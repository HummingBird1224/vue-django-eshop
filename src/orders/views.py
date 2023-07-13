from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import RedirectView, View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from notices.models import NoticeCategory, NoticeRead
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser
from .models import Order, OrderItem, ProvisionalOrderItemDesign
from .forms import UploadAIFileForm
from .serializers import OrderItemSerializer, OrderItemForEasyDraftSerializer, OrderSerializer, OrderWithoutCardInfoSerializer
from .tasks import send_notifications
from .pdf import (
    invoice,
    receipt,
    delivery,
)
from carts.models import Cart, CartItem
from mydesign.models import MyDesign, MyDesignDesign
from utils.payment_functions import (
    capture_from_order,
)
import io
from datetime import datetime, timedelta
import json


@method_decorator(login_required, name='dispatch')
class OrderHistoryView(ListView):
    """ 注文履歴のリスト表示
    TODO: ページング
    """

    template_name = "orders/order_history.html"
    model = Order
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user).exclude(state='new')


@method_decorator(login_required, name='dispatch')
class OrderHistoryItemView(DetailView):
    """ 注文履歴の個別情報表示
    """

    template_name = "orders/order_history_item.html"
    model = OrderItem

    def get_object(self):
        item = get_object_or_404(OrderItem, ref_code=self.kwargs['ref_code'])
        return item

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['static_url'] = settings.STATIC_URL
        return context


class OrderListAPIView(ListAPIView):

    serializer_class = OrderWithoutCardInfoSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).exclude(state='new')


@method_decorator(login_required, name='dispatch')
class OrderReorderView(DetailView):

    template_name = 'orders/reorder.html'
    model = OrderItem

    def get_object(self):
        item = get_object_or_404(OrderItem, ref_code=self.kwargs['ref_code'])
        if not item.is_reorderable() or \
            not item.design.state == 'confirmed':
            raise Http404()
        return item


class OrderItemReorderRetrieveAPIView(RetrieveAPIView):
    """ 再注文用のデータ取得API
    """

    serializer_class = OrderItemSerializer
    lookup_field = 'ref_code'

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(order__user=user).exclude(order__state='new')

    def retrieve(self, request, *args, **kwargs):
        res = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        res.data['thumbnail'] = instance.product.get_thumbnail_url()
        res.data['rendered_info'] = instance.render_extra_info()
        res.data['product_slug'] = instance.product.slug
        res.data['unit'] = instance.product.unit
        try:
            quantity = instance.product.options.filter(slug='quantity').first()
            cq = [item.value for item in quantity.items.all()]
            res.data['choosable_quantity'] = cq
        except Exception as e:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return res


class OrderItemReorderAPIView(APIView):
    """ 再注文API
    デザインの承認が行われている場合
    TODO: 注文数の変更
    """

    def post(self, request, format=None, **kwargs):
        cart = Cart.objects.get_or_create_from_request(request)
        oiref = kwargs.get('ref_code', None)
        oi = OrderItem.objects.filter(ref_code=oiref).first()
        options = request.data
        quantity = options['quantity']

        reorder = False
        if oi:
            if oi.order.user == request.user and \
               oi.is_reorderable() and \
               oi.design.state == 'confirmed':
                reorder = True
        if reorder:
            extra_info = options
            extra_info['reordered'] = True
            extra_info['reordered_from'] = oi.ref_code
            item = CartItem.objects.create(
                cart=cart,
                product=oi.product,
                quantity=quantity,
                extra_info=extra_info,
            )
            cart.update()
            return Response({"message": "Add {} to cart".format(item.product.name)}, status=status.HTTP_200_OK)
        return Response({'message': "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)


class OrderHistoryItemRetrieveAPIView(RetrieveAPIView):
    """ 注文履歴の個別情報取得API
    TODO: OrderItemRetrieveAPIViewと統合（フロントと統合が必要）
    """

    serializer_class = OrderItemSerializer
    lookup_field = 'ref_code'

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(order__user=user).exclude(order__state='new')

    def retrieve(self, request, *args, **kwargs):
        res = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        res.data['thumbnail'] = instance.product.get_thumbnail_url()
        if instance.product.is_active:
            res.data['product_url'] = instance.product.get_absolute_url()

        # DESIGN
        res.data['design']['comments'] = []
        if instance.design.comment:
            res.data['design']['comments'] = [c for c in instance.design.comment.split()]
        if res.data['design']['data']:
            res.data['design']['filename'] = res.data['design']['data'].split("/")[-1]
            res.data['design']['size'] = instance.design.human_readable_filesize()
        return res


class OrderDesignUploadAPIView(APIView):
    """ 注文のデザインアップロードAPI
    アップロードのみ、注文とデータの紐付けはまだ行わない
    以下は弾く
        デザインが確定しているもの
        注文全体が完了・キャンセルしているもの
    """

    parser_classes = (MultiPartParser, )

    def post(self, request, format=None, **kwargs):
        oiref = kwargs.get('ref_code', None)
        # form validation
        oi = OrderItem.objects.filter(ref_code=oiref).first()
        upload = False
        if oi and \
           oi.order.user == request.user and \
           oi.order.state == 'created' and \
           oi.design.state != 'confirmed':
            upload = True
        if upload:
            pro_design = oi.provisional_design
            form = UploadAIFileForm(request.POST, request.FILES, instance=pro_design)
            if form.is_valid():
                form.save()
                return Response({'message': "Successfully uploaded.",
                                 'data': pro_design.data.url,
                                 'size': pro_design.human_readable_filesize(),
                                 'id': pro_design.id}, status=status.HTTP_200_OK)
            return Response({'message': "Invalid form data.",
                             'errors': dict(form.errors.items())}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)


class OrderDesignUploadCompleteAPIView(APIView):
    """ 注文のデザインアップロード完了API
    注文とデータの紐付けを行う
    以下は弾く
        デザインが確定しているもの
        注文全体が完了・キャンセルしているもの
    """

    def post(self, request, format=None, **kwargs):
        oiref = kwargs.get('ref_code', None)
        oi = OrderItem.objects.filter(ref_code=oiref).first()
        data = json.loads(self.request.body)
        pro_design_id = data['id']
        pro_design = ProvisionalOrderItemDesign.objects.filter(id=pro_design_id).first()
        upload = False
        if oi and pro_design and \
           oi.order.user == request.user and \
           oi.order.state == 'created' and \
           oi.design.state != 'confirmed' and \
           pro_design.item.order.user == self.request.user:
            upload = True
        if upload:
            design = oi.design
            design.data = pro_design.data
            design.state = 'under_check'
            design.save()

            # NOTIFICATIONS
            context = {
                'user': self.request.user,
                'orderitem': oi,
                'expiry_date': datetime.today() + timedelta(days=settings.PAYMENT_EXPIRY_DAYS)
            }
            send_notifications(oi, 'upload', context)
            return Response({'message': "Successfully uploaded."}, status=status.HTTP_200_OK)
        return Response({'message': "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(login_required, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class OrderDesignUploadRedirectView(RedirectView):
    """ 注文のデザインアップロード完了 + リダイレクト
    同上
    """

    pattern_name = 'order_history'

    def get_redirect_url(self, *args, **kwargs):
        oiref = kwargs.get('ref_code', None)
        oi = OrderItem.objects.filter(ref_code=oiref).first()
        data = json.loads(self.request.body)
        pro_design_id = data['id']
        pro_design = ProvisionalOrderItemDesign.objects.filter(id=pro_design_id).first()
        upload = False
        if oi and pro_design:
            if oi.order.user == self.request.user and \
               oi.order.state == 'created' and \
               oi.design.state != 'confirmed' and \
               pro_design.item.order.user == self.request.user:
                upload = True
        if upload:
            design = oi.design
            design.data = pro_design.data
            design.state = 'under_check'
            design.save()
            messages.success(self.request, "入稿が完了しました", extra_tags="design-uploaded")

            # NOTIFICATIONS
            context = {
                'user': self.request.user,
                'orderitem': oi,
                'expiry_date': datetime.today() + timedelta(days=settings.PAYMENT_EXPIRY_DAYS)
            }
            send_notifications(oi, 'upload', context)
            data_import_category = NoticeCategory.objects.get(name='data import reminder')
            NoticeRead.objects.filter(notices__category_id=data_import_category.id,notices__noticereminder__orderitem_id=oi.id).update(read_at = datetime.now())

        return super().get_redirect_url() + "?uploaded=true"


@method_decorator(login_required, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class OrderDesignConfirmRedirectView(RedirectView):
    """ 注文のデザイン承認 & リダイレクト
    カード決済の確定も行う
        同一注文内の他の商品がキャンセル or デザインの承認が終わっている場合
    MyDesignのフラグが立ってないときMyDesignを作成
    """

    pattern_name = 'order_history'

    @transaction.atomic
    def get_redirect_url(self, *args, **kwargs):
        oiref = kwargs.get('ref_code', None)
        oi = OrderItem.objects.filter(ref_code=oiref).first()
        confirm = False
        if oi:
            if oi.order.user == self.request.user and \
               oi.order.state == 'created' and \
               oi.design.state != 'confirmed':
                confirm = True
        if confirm:
            design = oi.design
            design.state = 'confirmed'
            design.save()
            # 決済確定
            capture_from_order(oi.order)
            messages.success(self.request, "注文が完了しました！", extra_tags="design-confirmed")

            # MyDesign作成
            # if not oi.extra_info.get('from_mydesign', False):
            #     read_only_options = oi.extra_info
            #     read_only_options.pop('quantity')
            #     md = MyDesign.objects.create(
            #         user=self.request.user,
            #         product=oi.product,
            #         product_name=oi.product.name,
            #         size=oi.extra_info.get('size', {}),
            #         read_only_options=read_only_options,
            #         ordered_num=1,
            #     )
            #     MyDesignDesign.objects.create(
            #         mydesign=md,
            #         data=design.data
            #     )

            # NOTIFICATIONS
            context = {
                'user': self.request.user,
                'orderitem': oi,
                'expiry_date': datetime.today() + timedelta(days=settings.PAYMENT_EXPIRY_DAYS)
            }
            send_notifications(oi, 'confirm', context)

        # TODO: Get paramではなくMessageにする
        return super().get_redirect_url() + "?confirmed=true"


@method_decorator(login_required, name='dispatch')
class DocumentInvoiceView(View):
    """ 商品ごとの請求書の発行。
    タイミング：　仮決済が作成されたとき（注文確定後）
    """

    def get(self, *args, **kwargs):

        # SELECT ORDER ITEM
        ref = kwargs.get('ref_code', None)
        item = get_object_or_404(OrderItem, ref_code=ref)

        # VALIDATION
        if item.order.state == 'new':
            raise Http404

        # CREATE PDF
        buffer = io.BytesIO()
        invoice.draw_pdf(buffer, item)
        buffer.seek(0)
        return FileResponse(buffer, content_type='application/pdf', as_attachment=True)


@method_decorator(login_required, name='dispatch')
class DocumentReceiptView(View):
    """ 商品ごとの領収書の発行。
    タイミング：　支払いが完了したとき
    """

    def get(self, *args, **kwargs):

        # SELECT ORDER ITEM
        ref = kwargs.get('ref_code', None)
        item = get_object_or_404(OrderItem, ref_code=ref)

        # VALIDATION
        if not item.order.get_transaction().is_captured:
            raise Http404

        # CREATE PDF
        buffer = io.BytesIO()
        receipt.draw_pdf(buffer, item)
        buffer.seek(0)
        return FileResponse(buffer, content_type='application/pdf', as_attachment=True)


@method_decorator(login_required, name='dispatch')
class DocumentDeliveryView(View):
    """ 商品ごとの納品書の発行。
    タイミング：　納品完了後
    """

    def get(self, *args, **kwargs):

        # SELECT ORDER ITEM
        ref = kwargs.get('ref_code', None)
        item = get_object_or_404(OrderItem, ref_code=ref)

        # VALIDATION
        if item.delivery.state != 'delivered' or not item.order.get_transaction().is_captured:
            raise Http404
        elif not item.delivery.delivery_date:
            raise Http404

        # CREATE PDF
        buffer = io.BytesIO()
        delivery.draw_pdf(buffer, item)
        buffer.seek(0)
        return FileResponse(buffer, content_type='application/pdf', as_attachment=True)


class OrderItemCancelAPIView(APIView):
    """ 注文のキャンセルAPI
    条件
        デザインが承認されていない
        トランザクション完了してない
    決済の確定も行う
        同一注文内の他の商品がキャンセル or デザインの承認が終わっている場合
    TODO: カード決済対応
    """

    def post(self, request, format=None, **kwargs):
        oiref = kwargs.get('ref_code', None)
        oi = OrderItem.objects.filter(ref_code=oiref).first()
        cancel = False
        if oi:
            if oi.order.user == request.user and \
               oi.design.state != 'confirmed' and \
               oi.order.get_transaction().is_captured is False:
                cancel = True
        if cancel:
            old_total = oi.order.total
            oi.cancel_atomic()
            new_total = oi.order.total

            # NOTIFICATIONS
            context = {
                'user': self.request.user,
                'orderitem': oi,
                'refund': old_total - new_total,
                'expiry_date': datetime.today() + timedelta(days=settings.PAYMENT_EXPIRY_DAYS)
            }
            send_notifications(oi, 'cancel', context)
            return Response({"message": "cancelled"}, status=status.HTTP_200_OK)
        return Response({"message": "nothing to be cancelled"}, status=status.HTTP_400_BAD_REQUEST)


class OrderItemRetrieveAPIView(RetrieveAPIView):
    """ 注文履歴の個別情報取得API
    """

    serializer_class = OrderItemSerializer
    lookup_field = 'ref_code'

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(order__user=user).exclude(order__state='new')

    def retrieve(self, request, *args, **kwargs):
        res = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        res.data['thumbnail'] = instance.product.get_thumbnail_url()
        if instance.product.is_active:
            res.data['product_url'] = instance.product.get_absolute_url()

        # DESIGN
        res.data['design']['comments'] = []
        if instance.design.comment:
            res.data['design']['comments'] = [c for c in instance.design.comment.split()]
        if res.data['design']['data']:
            res.data['design']['filename'] = res.data['design']['data'].split("/")[-1]
            res.data['design']['size'] = instance.design.human_readable_filesize()
        return res


class EasyDraftInfoRetrieveAPIView(RetrieveAPIView):
    """ カンタン入稿の情報取得API
    """

    serializer_class = OrderItemForEasyDraftSerializer
    lookup_field = 'ref_code'

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(order__user=user).exclude(order__state='new')


class EasyDraftUploadAPIView(APIView):
    """ カンタン入稿のデータアップロードAPI
    """

    parser_classes = (MultiPartParser,)

    def post(self, request, format=None, **kwargs):
        oiref = kwargs.get('ref_code', None)
        # form validation
        oi = OrderItem.objects.filter(ref_code=oiref).first()
        upload = False
        if oi and \
           oi.order.user == request.user and \
           oi.order.state == 'created' and \
           oi.design.state != 'confirmed':
            upload = True
        if upload:
            pro_design = oi.provisional_design
            form = UploadAIFileForm(request.POST, request.FILES, instance=pro_design)
            if form.is_valid():
                form.save()
                design = oi.design
                design.data = pro_design.data
                design.state = 'under_check'
                design.save()
                # NOTIFICATIONS
                context = {
                    'user': self.request.user,
                    'orderitem': oi,
                    'expiry_date': datetime.today() + timedelta(days=settings.PAYMENT_EXPIRY_DAYS)
                }
                send_notifications(oi, 'upload', context)
                data_import_category = NoticeCategory.objects.get(name='data import reminder')
                NoticeRead.objects.filter(
                    read_at=None,
                    notices__category=data_import_category,
                    notices__noticereminder__orderitem_id=oi
                ).update(read_at=datetime.now())
                return Response({'message': "Successfully uploaded."}, status=status.HTTP_200_OK)
        return Response({'message': "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)


class OrderDesignResetAPIView(APIView):
    """ デザインの初期化（削除）API
    """

    def post(self, request, format=None, **kwargs):
        oiref = kwargs.get('ref_code', None)
        oi = OrderItem.objects.filter(ref_code=oiref).first()
        reset = False
        if oi and \
           oi.order.user == request.user and \
           oi.order.state == 'created' and \
           oi.design.state != 'confirmed':
            reset = True
        if reset:
            design = oi.design
            design.data = ''
            design.state = 'not_submitted'
            design.save()
            return Response({'message': "Successfully reset design."}, status=status.HTTP_200_OK)
        return Response({'message': "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
