import os
import csv

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import transaction, models
from django.db.models import Q
from django.shortcuts import reverse, redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from orders.models import Order, OrderItem, LogOrderItemStateUpdate
from notices.models import NoticePost, NoticeCategory, NoticeRead, NoticeReminder
from notices.forms import NoticePostModelForm
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, CreateView
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from rest_framework import status, pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import RetrieveAPIView, ListAPIView
from datetime import datetime, timedelta
import re
from billing.models import Transaction
from products.models import ProductCategory, ProductTag, Product, ProductImage, ProductOption, ProductOptionItem
from notices.serializers import NoticePostSerializer

from .forms import OrderItemForm, OrderItemCancelForm
from .tasks import send_notifications, create_notice, send_prompts

from utils.payment_functions import (
    capture_from_order,
)


"""
# states
not_submitted: 0
under_check: 1
resubmission_request: 2
checked: 3
confirmed: 4
printing: 5
shipped: 6
delivered: 7
cancelled: 8
"""

User = get_user_model()

design_state = ['not_submitted', 'under_check', 'resubmission_request', 'checked', 'confirmed']
delivery_state = ['printing', 'shipped', 'delivered']
all_state = design_state + delivery_state + ['cancelled']

design_state_display = ['未入稿', '確認中', '再入稿依頼', '確認済', '承認済']
delivery_state_display = ['印刷中', '発送済', '宅配済']
all_state_display = design_state_display + delivery_state_display + ['キャンセル済']

all_state_num = {state: i for i, state in enumerate(all_state)}


class State:
    def __init__(self, state, display_state):
        self.state = state
        self.display_state = display_state


def index(request):
    order_list = Order.objects.all()[:5]
    output = ', '.join([o.user for o in order_list])
    return HttpResponse(output)

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_page': self.page.number,
            'results': data
        })


@method_decorator(staff_member_required, name='dispatch')
class InternalOrderListView(ListView):

    template_name = "internal/orders/order_list.html"
    model = Order
    paginate_by = 20

    def get_queryset(self):
        if 'state' not in self.request.GET:
            queryset = Order.objects
        else:
            state = self.request.GET.get('state')
            if state == 'cancelled':
                queryset = Order.objects.filter(items__payment='cancelled')
            elif state in design_state + delivery_state:
                if state == 'confirmed':
                    order_item_ids = OrderItem.objects.filter(design__state='confirmed').filter(delivery__state='unassigned').values_list('id', flat=True)
                elif state in design_state:
                    order_item_ids = OrderItem.objects.filter(design__state=state).values_list('id', flat=True)
                elif state in delivery_state:
                    order_item_ids = OrderItem.objects.filter(delivery__state=state).values_list('id', flat=True)
                queryset = Order.objects.exclude(items__payment='cancelled').filter(items__id__in=order_item_ids)
            else:
                queryset = Order.objects
        queryset = queryset.exclude(state='new')
        if self.request.GET.get('q', None):
            q = self.request.GET.get('q')
            if queryset.filter(ref_code=q).union(queryset.filter(ref_code__contains=q)).count() > 0:
                queryset = queryset.filter(ref_code=q).union(queryset.filter(ref_code__contains=q))
            else:
                queryset = queryset.filter(user__company_name__icontains=q).union(queryset.filter(user__name__icontains=q))

        queryset = queryset.order_by('-created_at')
        if 'order' in self.request.GET:
            order = self.request.GET.get('state')
            if order == 'shipping_date':
                queryset = queryset.order_by('-shipping_date')

        if 'desc' in self.request.GET and int(self.request.GET.get('desc')) == 0:
            queryset = queryset.reverse()
        return queryset

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(object_list=None, *args, **kwargs)
        context['state'] = self.request.GET.get('state') if 'state' in self.request.GET else 'all'
        context['display_state'] = all_state_display[all_state.index(context['state'])] \
            if context['state'] in all_state else None
        context['order'] = self.request.GET['order'] if 'order' in self.request.GET else 'created_at'
        context['desc'] = self.request.GET.get('desc') if 'desc' in self.request.GET else '1'
        context['q'] = self.request.GET.get('q') if 'q' in self.request.GET else ''
        context['all_state'] = [State(all_state[i], all_state_display[i]) for i in range(len(all_state))]
        return context


@method_decorator(staff_member_required, name='dispatch')
class InternalOrderItemDetailView(DetailView, FormMixin):

    template_name = "internal/orders/order_detail.html"
    model = OrderItem
    form_class = OrderItemForm

    def get_success_url(self):
        return reverse('internal:order_detail', kwargs={'ref_code': self.get_object().ref_code})

    def get_object(self):
        item = get_object_or_404(OrderItem, ref_code=self.kwargs['ref_code'])
        return item

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        item = self.get_object()
        if 'order_item_form' in request.POST:
            form = OrderItemForm(**self.get_form_kwargs())
            if form.is_valid():
                state = int(form.data['state'])
                old_state_string = self._item_state_to_inner_state(item)

                # Validations
                is_valid = True
                if item.payment == 'cancelled':
                    messages.error(request, "キャンセルされているため変更はできません。")
                    is_valid = False
                if 1 <= state <= 3:
                    if not (item.design.data or form.cleaned_data.get('data')):
                        messages.error(request, "デザインデータが必要です。")
                        is_valid = False
                if 6 <= state:
                    if not form.cleaned_data.get('shipping_date'):
                        messages.error(request, "発送日の登録が必要です。")
                        is_valid = False
                if state == 7:
                    if not form.cleaned_data.get('delivery_date'):
                        messages.error(request, "宅配日の登録が必要です。")
                        is_valid = False

                if item.order.get_transaction().is_captured and state <= 3:
                    messages.error(request, "すでに決済が完了しているため、元のステータスには戻せません。")
                    is_valid = False

                if not item.order.get_transaction().is_captured and state >= 5:
                    messages.error(request, "デザインの承認をしてください。")
                    is_valid = False

                if not is_valid:
                    return self.form_invalid(form)

                item.delivery.company = form.data['company']
                item.delivery.tracking_code = form.data['tracking_code']
                if form.data['shipping_date']:
                    item.delivery.shipping_date = form.data['shipping_date']
                if form.data['delivery_date']:
                    item.delivery.delivery_date = form.data['delivery_date']
                if request.FILES.get('data'):
                    item.design.data = request.FILES['data']
                item.design.comment = form.data['comment']

                # デザイン変更の場合
                if 0 <= state <= 4:
                    # デザイン状況更新 + 配送状況を未設定に
                    item.design.state = all_state[state]
                    item.delivery.state = 'unassigned'
                    item.design.save()
                    item.delivery.save()
                    if state == 4 and item.payment == 'pending':  # if design confirmed
                        item.payment = 'confirmed'
                        item.save()
                        capture_from_order(item.order)

                # 配送変更の場合
                if 5 <= state <= 7:
                    # 配送状況更新 + デザイン状況を未設定に
                    item.delivery.state = all_state[state]
                    item.design.state = 'confirmed'
                    item.delivery.save()
                    item.design.save()

                if state in [2, 3, 4, 5, 6, 7] and old_state_string != all_state[state]:
                    # 2: resubmission_request, 3: checked, 4: confirmed
                    # 5: printing, 6: shipped, 7: delivered
                    self._send_notification(item, all_state[state])
                    self._create_notice(item, all_state[state])
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        elif 'order_item_cancel_form' in request.POST:
            self._cancel(item)
            return redirect('internal:order_detail', item.ref_code)
        elif 'order_item_draftprompt_form' in request.POST:
            self._send_prompt(item, 'draftprompt') # 8:入稿催促
            item.draftprompt_edited_at=timezone.now()
            item.save()
            return self.form_valid(item)
        elif 'order_item_payprompt_form' in request.POST:
            self._send_prompt(item, 'payprompt') # 9:振込催促
            item.payprompt_edited_at=timezone.now()
            item.save()
            return self.form_valid(item)

    def _cancel(self, item):
        if item.payment in ['pending', 'confirmed']:
            item.cancel_atomic()

    def _create_notice(self, item, action):
        create_notice(item, action)

    def _send_notification(self, item, action):
        context = {
            'host': '{}://{}'.format(self.request.scheme, self.request.get_host()),
            'design_comments': [c for c in item.design.comment.split()],
            'user': item.order.user,
            'orderitem': item,
            'expiry_date': datetime.today() + timedelta(days=settings.PAYMENT_EXPIRY_DAYS)
        }
        send_notifications(item, action, context)

    def _send_prompt(self, item, action):
        context = {
            'host': '{}://{}'.format(self.request.scheme, self.request.get_host()),
            'user': item.order.user,
            'orderitem': item,
            'expiry_date': datetime.today() + timedelta(days=settings.PAYMENT_EXPIRY_DAYS)
        }
        send_prompts(item, action, context)

    def _item_state_to_inner_state(self, item):
        if item.payment == 'cancelled':
            return 'cancelled'
        if item.delivery.state == 'unassigned':
            return item.design.state
        return item.delivery.state

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        form = OrderItemForm(initial={
            'company': self.object.delivery.company,
            'tracking_code': self.object.delivery.tracking_code,
            'shipping_date': self.object.delivery.shipping_date,
            'delivery_date': self.object.delivery.delivery_date,
            'comment': self.object.design.comment,
            'state': all_state_num[self.object.internal_state],
        })
        # form.fields['state'].initial = all_state_num[self.object.internal_state]
        cancel_form = OrderItemCancelForm()
        context['form'] = form
        context['cancel_form'] = cancel_form
        context['current_state'] = all_state_num[self.object.internal_state]
        context['data_url'] = self.object.design.data.url if self.object.design.data else None
        context['data_file_name'] = os.path.basename(context['data_url']) if context['data_url'] else None
        return context


@method_decorator(staff_member_required, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class CompleteBankTransferAPI(APIView):
    """銀行振込の完了API
    スタッフのみアクセス可能
    銀行振込の完了をする
    """

    @transaction.atomic
    def post(self, request, ref_code, format=None):
        order = Order.objects.filter(ref_code=ref_code).first()
        transaction = Transaction.objects.filter(order=order).first()
        if order and transaction:
            transaction.is_captured = True
            transaction.save()
            bank_transfer_category = NoticeCategory.objects.get(name='bank transfer reminder')
            NoticeRead.objects.filter(
                read_at=None,
                notices__category=bank_transfer_category,
                notices__noticereminder__orderitem_id__in=list(order.items.values_list('id',flat=True))
            ).update(read_at=datetime.now())
        return Response({'message': 'success'}, status=status.HTTP_200_OK)


@method_decorator(staff_member_required, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class UncompleteBankTransferAPI(APIView):
    """銀行振込の完了取り消しAPI
    スタッフのみアクセス可能
    銀行振込の完了を取り消す
    """

    @transaction.atomic
    def post(self, request, ref_code, format=None):
        print("hello")
        order = Order.objects.filter(ref_code=ref_code).first()
        transaction = Transaction.objects.filter(order=order).first()
        if order and transaction:
            transaction.is_captured = False
            transaction.save()
            """
            bank_transfer_category = NoticeCategory.objects.get(name='bank transfer reminder')
            for orderitem in order.items:
                NoticeReminder.objects.create(category_id=bank_transfer_category.id,orderitem_id=orderitem)
            """
        return Response({'message': 'success'}, status=status.HTTP_200_OK)


class OrderItemStateLogCsvAPIView(APIView):
    def get(self, request):
        order_item_log = LogOrderItemStateUpdate.objects.all()
        response = HttpResponse(content_type='text/csv')

        fields = [
            'order_item_id', 'order_id', 'state', 'prev_state', 'updated_date', 'ref_code', 'product', 'user', 'company',
            'shipping_date', 'delivery_date', 'order_date', 'delivery_company', 'tracking_code',
            'postal_code', 'prefecture', 'address', 'tel',
            'product_total_price', 'mold_price', 'plate_price', 'tax', 'total_price'
        ]
        columns = [
            'item__id', 'item__order__id', 'val', 'prev_val', 'created_at', 'item__ref_code', 'item__product_name',
            'item__order__user__name', 'item__order__user__company_name',
            'item__delivery__shipping_date', 'item__delivery__delivery_date', 'item__created_at',
            'item__delivery__company', 'item__delivery__tracking_code',
            'item__delivery__postal_code', 'item__delivery__prefecture', 'item__delivery__address',
            'item__delivery__tel', 'item__prices'
        ]

        writer = csv.writer(response)
        writer.writerow(fields)
        for row in order_item_log.values_list(*columns):
            writer.writerow(row[:18] + tuple([
                row[18].get('product_total', 0),
                row[18].get('mold_price', 0),
                row[18].get('plate_price', 0),
                row[18].get('tax', 0),
                row[18].get('total', 0),
            ]))

        return response


# TODO: socketioでリアルタイム計測
@method_decorator(staff_member_required, name='dispatch')
class DataAnalyticsView(TemplateView):

    template_name = "internal/analytics/analytics_home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        users = User.objects.all().exclude(is_admin=True)
        context['num_user'] = len(users)
        context['num_use_with_address'] = len(['' for u in users if u.get_default_delivery_address()])

        orders = Order.objects.all()
        context['num_orders'] = len(orders)
        context['num_completed_orders'] = len(orders.exclude(state='new'))

        return context


@method_decorator(staff_member_required, name='dispatch')
class InternalNoticePostListView(ListView):

    template_name = "internal/notices/notice_post_list.html"
    model = NoticePost

class NoticePOSTListAPIView(ListAPIView):
    queryset = NoticePost.objects.order_by('created_at').reverse()
    serializer_class = NoticePostSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            queryset = queryset.filter(Q(post_title__icontains=keyword) | Q(text__icontains=keyword))
        return queryset

@method_decorator(staff_member_required, name='dispatch')
class InternalNoticePostDetailView(DetailView, FormMixin):

    template_name = "internal/notices/notice_post_detail.html"
    model = NoticePost
    form_class = NoticePostModelForm

    def get_success_url(self):
        return reverse('internal:notice_post_detail', args=(self.get_object().pk,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(initial={
            'post_title': self.object.post_title,
            'text': self.object.text,
            'category': self.object.category
        })
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if request.POST['notice_action'] == '保存する':
            post = self.get_object()
            if form.is_valid():
                post.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        elif request.POST['notice_action'] == '公開する':
            if form.is_valid():
                category = NoticeCategory.objects.get(message=form.cleaned_data['category'])
                post,created = NoticePost.objects.get_or_create(
                    post_title = form.cleaned_data['post_title'],
                    text = form.cleaned_data['text'],
                    category_id = category.id
                )
                post.published_at=timezone.now()
                post.save()
                [ post.notice_ptr.users.add(i)  for i in User.objects.filter(is_active=True)]
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

class InternalNoticePostCreateView(CreateView):
    template_name = "internal/notices/notice_post_detail.html"
    model = NoticePost
    form_class = NoticePostModelForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        # TODO: DRY
        if request.POST['notice_action'] == '保存する':
            if form.is_valid():
                form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        elif request.POST['notice_action'] == '公開する':
            if form.is_valid():
                post = form.save()
                post.published_at=timezone.now()
                post.save()
                [ post.notice_ptr.users.add(i)  for i in User.objects.filter(is_active=True)]
                self.object = post
                return HttpResponseRedirect(self.get_success_url())
            else:
                return self.form_invalid(form)


    def get_success_url(self):
        return reverse('internal:notice_post_detail', args=(self.object.pk,))

class InternalCreateCustomProductView(TemplateView):

    template_name = "internal/custom/create_custom_product.html"


@method_decorator(staff_member_required, name='dispatch')
class CustomProductFormAPIView(APIView):

    def get(self, request, format=None, **kwargs):
        data = {}
        data['users'] = [{'id': u.id, 'name': u.get_fullname()} for u in User.objects.all()]
        return Response(data, status=status.HTTP_200_OK)


@method_decorator(staff_member_required, name='dispatch')
class AddCustomProductAPIView(APIView):
    """ カスタム商品追加API
    管理画面のフォームからPOST
    """

    def post(self, request, format=None, **kwargs):
        data = request.data

        try:
            # user_data = data.get('user', {})
            # user_id = user_data.get('id')
            # user = User.objects.filter(id=user_id).first()
            #
            # product_data = data.get('product', {})
            # product_name = product_data.get('product_name')
            # product_detail = product_data.get('product_detail')
            # product_unit = product_data.get('product_unit')
            #
            # info_data = data.get('info', {})
            # info_min = info_data.get('min_ordering_quantity')
            # info_max = info_data.get('max_ordering_quantity')
            # info_first = info_data.get('estimated_shipping_date_first')
            # info_repeat = info_data.get('estimated_shipping_date_repeat')
            # info_design = info_data.get('is_design_necessary')
            # info_easy = info_data.get('is_easy_draft_available')
            #
            # option_data = data.get('options', {})
            # size_data= option_data.get('size', {})
            # size_items = option_data.get('items', [])
            # if size_items:
            #     size_name = size_items[0].get('name')
            #     size_height = size_items[0].get('height')
            #     size_width = size_items[0].get('width')
            #     size_depth = size_items[0].get('depth')
            #
            # quantity_data= option_data.get('quantity', {})
            # quantity_items = option_data.get('items', [])
            #
            # note_data = data.get('notes', [])
            #
            # order_data = data.get('order', {})
            #
            # order_quantity = order_data.get('quantity')
            #
            # delivery_data = order_data.get('delivery', {})
            # delivery_name = delivery_data.get('name')
            # delivery_postal_code = delivery_data.get('postal_code')
            # delivery_prefecture = delivery_data.get('prefecture')
            # delivery_city = delivery_data.get('city')
            # delivery_building = delivery_data.get('building')
            # delivery_tel = delivery_data.get('tel')
            #
            # billing_data = order_data.get('billing', {})
            # billing_name = billing_data.get('name')
            # billing_postal_code = billing_data.get('postal_code')
            # billing_prefecture = billing_data.get('prefecture')
            # billing_city = billing_data.get('city')
            # billing_building = billing_data.get('building')
            # billing_tel = billing_data.get('tel')
            pass
        except Exception as e:
            return Response({'message': 'success'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'success'}, status=status.HTTP_200_OK)


@method_decorator(staff_member_required, name='dispatch')
class ProductCreateView(TemplateView):

    template_name = 'internal/products/product_create.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data( **kwargs)
        ctx['category'] = ProductCategory.objects.all()
        ctx['tag'] = ProductTag.objects.all()
        return ctx


@method_decorator(staff_member_required, name='dispatch')
class ProductCategoryAndTagListAPIView(APIView):

    def get(self, request):
        categories = [{"id": c.id, "name": c.__str__()} for c in ProductCategory.objects.all()]
        tags = [{"id": t.id, "name": t.name} for t in ProductTag.objects.all()]
        return Response({'categories': categories, 'tags': tags}, status=status.HTTP_200_OK)


@method_decorator(staff_member_required, name='dispatch')
class ProductCreateAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def dispatch(self, request, *args, **kwargs):
        res = super().dispatch(request, *args, **kwargs)
        return res

    @transaction.atomic
    def post(self, request, format=None, *args, **kwargs):
        data = request.data

        name = data['name']
        slug = data['slug']
        category_id = data['category']
        tags_id = data.get('tags', [])
        overview = data['overview']
        unit = data['unit']

        can_order_on_site = 'on' == data.get('can_order_on_site', False)
        is_contact_required = 'on' == data.get('is_contact_required', False)
        can_order_sample = 'on' == data.get('can_order_sample', False)
        min_ordering_quantity = data['min_ordering_quantity']
        max_ordering_quantity = data['max_ordering_quantity']
        estimated_shipping_date_first = data['estimated_shipping_date_first']
        estimated_shipping_date_repeat = data['estimated_shipping_date_repeat']
        can_select_original_size = 'on' == data.get('can_select_original_size', False)
        is_design_necessary = 'on' == data.get('is_design_necessary', False)
        choosable_color = data['choosable_color']
        sizelimit_height = data['sizelimit_height']
        sizelimit_width = data['sizelimit_width']
        sizelimit_depth = data['sizelimit_depth']

        category = ProductCategory.objects.filter(id=category_id).first()

        required_list = [name, slug, overview, category, unit,
                         min_ordering_quantity, max_ordering_quantity,
                         estimated_shipping_date_first, estimated_shipping_date_repeat,
                         choosable_color]
        if not all(required_list):
            return Response({"message": "Invalid form value."}, status=status.HTTP_400_BAD_REQUEST)
        # notes
        notes = {"name": "備考", "extra": []}
        re_note_title = re.compile("note_(\d+)_title")
        for i in range(1, len([key for key in data.keys() if re.match(re_note_title, key)]) + 1):
            title = data.get("note_" + str(i) + "_title", "")
            content = data.get("note_" + str(i) + "_content", "")
            notes["extra"].append({"key": title, "value": content})
        # CREATE PRODUCT
        product = Product.objects.create(
            name=name,
            slug=slug,
            category=category,
            overview=overview,
            unit=unit,
        )
        for tag in [ProductTag.objects.filter(id=_id).first() for _id in tags_id if ProductTag.objects.filter(id=_id).first()]:
            product.tags.add(tag)
        product.save()

        # CREATE INFO
        info = product.info
        info.can_order_on_site = can_order_on_site
        info.is_contact_required = is_contact_required
        info.can_order_sample = can_order_sample
        info.min_ordering_quantity = min_ordering_quantity
        info.max_ordering_quantity = max_ordering_quantity
        info.estimated_shipping_date_first = estimated_shipping_date_first
        info.estimated_shipping_date_repeat = estimated_shipping_date_repeat
        info.can_select_original_size = can_select_original_size
        info.is_design_necessary = is_design_necessary
        info.notes = notes
        size_limit = {"height": sizelimit_height,
                      "width": sizelimit_width}
        if sizelimit_depth:
            size_limit["depth"] = sizelimit_depth
        info.size_limit = size_limit
        info.shipping_area = {"exclude": False, "prefectures": ["東京", "神奈川", "静岡", "埼玉", "千葉"]}
        info.choosable_color = {"name": "印刷色", "extra": "", "image": "", "value": choosable_color}
        info.save()

        # CREATE IMAGE
        re_img = re.compile("image_(\d+)$")
        for i in range(1, len([key for key in data.keys() if re.match(re_img, key)]) + 1):
            if data.get("image_" + str(i)):
                img = data["image_" + str(i)]
                hover = 'on' == data.get("image_" + str(i) + "_hover", False)
                ProductImage.objects.create(
                    product=product,
                    image=img,
                    is_hover_image=hover,
                    position=i,
                )

        # CREATE OPTION
        re_option = re.compile("option_name_(\d+)$")
        option_num = len([key for key in data.keys() if re.match(re_option, key)])
        for i in range(1, option_num + 1):
            o_name = data["option_name_" + str(i)]
            o_slug = data["option_slug_" + str(i)]
            o_detail = data["option_detail_" + str(i)]
            o_position = data["option_ordering_" + str(i)]
            o_widget = data["option_widget_" + str(i)]
            re_item = re.compile("option_name_" + str(i) + "_alter_(\d+)$")
            item_num = len([key for key in data.keys() if re.match(re_item, key)])

            if not all([o_name, o_slug, o_position, o_widget]):
                return Response({"message": "Invalid form value."}, status=status.HTTP_400_BAD_REQUEST)

            option = ProductOption.objects.create(
                product=product,
                slug=o_slug,
                name=o_name,
                detail=o_detail,
                position=o_position,
                widget_type=o_widget
            )

            for j in range(1, item_num + 1):
                i_name = data["option_name_" + str(i) + "_alter_" + str(j)]
                i_delimiter = data["option_delim_" + str(i) + "_alter_" + str(j)]
                i_value = data["option_val_" + str(i) + "_alter_" + str(j)]
                i_detail = data["option_detail_" + str(i) + "_alter_" + str(j)]
                i_image = data["option_image_" + str(i) + "_alter_" + str(j)]
                i_default = "on" == data.get("option_default_" + str(i) + "_alter_" + str(j), False)
                i_position = data["option_ordering_" + str(i) + "_alter_" + str(j)]

                if not all([i_name, i_value, i_position]):
                    return Response({"message": "Invalid form value."}, status=status.HTTP_400_BAD_REQUEST)

                ProductOptionItem.objects.create(
                    option=option,
                    name=i_name,
                    delimiter=i_delimiter,
                    value=i_value,
                    detail=i_detail,
                    image=i_image,
                    is_default=i_default,
                    position=i_position,
                )
        return Response({"message": "Successfully Created."}, status=status.HTTP_200_OK)
