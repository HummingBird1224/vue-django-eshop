from django.db import transaction
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.utils.http import urlencode
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic.base import TemplateView, RedirectView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from accounts.models import (BillingAddress,
                             DeliveryAddress)
from carts.models import Cart
from products.models import Product
from orders.models import (Order,
                           OrderDeliveryAddress,
                           OrderBillingAddress,
                           OrderItem)
from orders.serializers import OrderSerializer
from mydesign.models import MyDesign
from utils.payjp_functions import *
from utils.payment_functions import capture_from_order
from .models import Transaction
from .forms import DeliveryAddressCreationForm, BillingAddressCreationForm
from .tasks import send_notifications
from datetime import datetime, timedelta
import uuid
import re
from math import ceil
import logging


logger = logging.getLogger(__name__)


class BillingView(TemplateView):
    """決済画面のテンプレート表示
    orderが
    - 存在しない
    - 他ユーザーのもの
    - 最新のものではない
    場合カート画面にリダイレクト
    """

    template_name = "billing/billing.html"

    def get(self, request, *args, **kwargs):
        ref_code = request.GET.get("oid")
        try:
            order = Order.objects.get(ref_code=ref_code)
            current_order = Order.objects.get_current_order(request)
            if not current_order or order != current_order or current_order.state != 'new':
                return redirect('cart')
            if request.user.is_authenticated:
                order.user = request.user
                order.save()
                self.create_addresses(request, order)
        except ObjectDoesNotExist:
            return redirect('cart')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_id'] = self.request.GET.get("oid")
        return context

    def create_addresses(self, request, order):
        # デフォルト住所があってOrderに住所がない場合配送先割り当て
        if not order.delivery_address.postal_code \
            and request.user.get_default_delivery_address():
            order_delivery = order.delivery_address
            default_delivery_address = request.user.get_default_delivery_address()
            order_delivery.name = default_delivery_address.name
            order_delivery.postal_code = default_delivery_address.postal_code
            order_delivery.prefecture = default_delivery_address.prefecture
            order_delivery.city = default_delivery_address.city
            order_delivery.building = default_delivery_address.building
            order_delivery.tel = default_delivery_address.tel
            order_delivery.save()

            for item in order.get_order_items():
                item_delivery = item.delivery
                item_delivery.address = default_delivery_address
                item_delivery.name = default_delivery_address.name
                item_delivery.postal_code = default_delivery_address.postal_code
                item_delivery.prefecture = default_delivery_address.prefecture
                item_delivery.city = default_delivery_address.city
                item_delivery.building = default_delivery_address.building
                item_delivery.tel = default_delivery_address.tel
                item_delivery.save()

        if not order.billing_address.postal_code \
            and request.user.get_default_billing_address():
            order_billing = order.billing_address
            default_billing_address = request.user.get_default_billing_address()
            order_billing.name = default_billing_address.name
            order_billing.postal_code = default_billing_address.postal_code
            order_billing.prefecture = default_billing_address.prefecture
            order_billing.city = default_billing_address.city
            order_billing.building = default_billing_address.building
            order_billing.tel = default_billing_address.tel
            order_billing.save()
        elif not order.billing_address.postal_code \
            and not request.user.get_default_billing_address() \
            and request.user.get_default_delivery_address():
            # デフォルトがないのでデフォルト配送先をもとに作成
            default_delivery = request.user.get_default_delivery_address()
            ba = BillingAddress.objects.create(
                user=default_delivery.user,
                name=default_delivery.name,
                postal_code=default_delivery.postal_code,
                prefecture=default_delivery.prefecture,
                city=default_delivery.city,
                building=default_delivery.building,
                tel=default_delivery.tel,
                is_default=True,
            )
            order_billing = order.billing_address
            order_billing.name = ba.name
            order_billing.postal_code = ba.postal_code
            order_billing.prefecture = ba.prefecture
            order_billing.city = ba.city
            order_billing.building = ba.building
            order_billing.tel = ba.tel
            order_billing.save()


class GetOrderInfoAPIView(APIView):
    """orderの情報取得API
    Billing Viewで表示したテンプレート内で使用
    """

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        order = Order.objects.get_current_order(request)
        if not order:
            return JsonResponse({"message": "Cannot find the order."},
                                status=400)

        # RETURN INFO ABOUT EACH ITEMS
        items = []
        for item in order.get_order_items():
            extra_info = {}
            extra_info['size'] = {'label': 'サイズ', 'value': item.size_str}
            extra_info['quantity'] = {'label': '注文数', 'value': item.quantity}
            extra_info['color_num'] = {'label': '色数', 'value': item.extra_info['color_num']}
            # # TODO: product extra_infoから
            # for k, v in item.extra_info.items():
            #     extra_info[k] = {'label': EXTRA_LABELS[k], 'value': v}
            items.append({
                'ref_code': item.ref_code,
                'product_name': item.product_name,
                'thumbnail': item.product.get_thumbnail_url(),
                'url': item.product.get_absolute_url(),
                'quantity': item.quantity,
                'extra': extra_info,
                'unit_price': item.prices['unit_price'],
                'total': item.prices['total'],
            })

        # ADDRESSES
        delivery_address = None if not order.delivery_address else {
            'full_name': order.delivery_address.get_full_name(),
            'postal_code': order.delivery_address.postal_code,
            'prefecture': order.delivery_address.prefecture,
            'city': order.delivery_address.city,
            'building': order.delivery_address.building,
            'tel': order.delivery_address.tel,
        }
        billing_address = None if not order.billing_address else {
            'full_name': order.billing_address.get_full_name(),
            'postal_code': order.billing_address.postal_code,
            'prefecture': order.billing_address.prefecture,
            'city': order.billing_address.city,
            'building': order.billing_address.building,
            'tel': order.billing_address.tel,
        }

        # RESPONSE DATA
        data = {
            'ref_code': order.ref_code,
            'product_total': order.product_total,
            'plate_total': order.plate_total,
            'mold_total': order.mold_total,
            'shipping_total': order.shipping_total,
            'tax_total': order.tax_total,
            'total': order.total,
            'currency': order.currency,
            'items': items,
            'delivery_address': delivery_address,
            'billing_address': billing_address,
        }
        return JsonResponse(data, status=200)


@method_decorator(require_POST, name='dispatch')
class CreateOrderRedirectView(RedirectView):
    """order作成
    POST/Redirect/GET
    全ての処理が完了するまで、DBの変更なし（transaction.atomic）
    """

    @transaction.atomic
    def get_redirect_url(self, *args, **kwargs):
        cart = Cart.objects.get_from_request(self.request)

        # DELETE OLD CART ITEMS AND BRING JUST ONE ITEM TO BILLING
        # for item in cart.get_cart_items().order_by('-created_at')[1:]:
        #     item.delete()

        # UPDATE CART
        cart.update()

        # SET REF CODE
        if self.request.user.is_authenticated:
            ref_code = str(self.request.user.id) + '-' + '-'.join(str(datetime.now().timestamp()).split("."))
        else:
            # TODO: CHANGE THIS TO NUMBER BASED REF CODE!
            ref_code = "".join(str(uuid.uuid4()).split("-"))

        # SET DELIVERY/BILLING ADDRESS TO DEFAULT ONE
        default_delivery_address, default_billing_address = None, None
        if self.request.user.is_authenticated:
            default_delivery_address = self.request.user.get_default_delivery_address()
            default_billing_address = self.request.user.get_default_billing_address()

        # GET REQUEST INFO
        stored_request = Order.objects.stored_request(self.request)

        # ORDER CREATION
        order = Order.objects.create(
            ref_code=ref_code,
            user=self.request.user if self.request.user.is_authenticated else None,
            product_total=cart.get_product_total(),
            plate_total=cart.get_plate_total(),
            mold_total=cart.get_mold_total(),
            shipping_total=cart.get_shipping_total(),
            tax_total=cart.get_tax(),
            total=cart.get_total(),
            state="new",
            stored_request=stored_request,
        )

        order_delivery = OrderDeliveryAddress.objects.create(order=order)
        order_billing = OrderBillingAddress.objects.create(order=order)

        # SET ADDRESS FOR ORDER
        if default_delivery_address:
            order_delivery.name = default_delivery_address.name
            order_delivery.postal_code = default_delivery_address.postal_code
            order_delivery.prefecture = default_delivery_address.prefecture
            order_delivery.city = default_delivery_address.city
            order_delivery.building = default_delivery_address.building
            order_delivery.tel = default_delivery_address.tel
            order_delivery.save()
        if default_billing_address:
            order_billing.name = default_billing_address.name
            order_billing.postal_code = default_billing_address.postal_code
            order_billing.prefecture = default_billing_address.prefecture
            order_billing.city = default_billing_address.city
            order_billing.building = default_billing_address.building
            order_billing.tel = default_billing_address.tel
            order_billing.save()

        # MAKE IT CURRENT ORDER
        Order.objects.set_current_order(self.request, ref_code)

        # MAKE ORDER ITEMS
        for i, item in enumerate(cart.get_cart_items()):
            # TODO: DELETE THIS AND SIMPLY DO
            #       prices=item.prices
            item_prices = {
                'product_total': item.product_total,
                'plate_price': item.plate_price,
                'mold_price': item.mold_price,
                'unit_price': item.unit_price,
                'shipping_price': item.shipping_price,
                'subtotal': item.subtotal,
                'tax': item.tax,
                'total': item.total
            }
            orderitem = OrderItem.objects.create(
                order=order,
                ref_code=ref_code + '-' + "{:04d}".format(i + 1),
                product=item.product,
                product_name=item.product.name,
                product_slug=item.product.slug,
                quantity=item.quantity,
                prices=item_prices,
                extra_info=item.extra_info,
            )
            # SET ADDRESS FOR ITEMS
            if default_delivery_address:
                item_delivery = orderitem.delivery
                item_delivery.address = default_delivery_address
                item_delivery.name = default_delivery_address.name
                item_delivery.postal_code = default_delivery_address.postal_code
                item_delivery.prefecture = default_delivery_address.prefecture
                item_delivery.city = default_delivery_address.city
                item_delivery.building = default_delivery_address.building
                item_delivery.tel = default_delivery_address.tel
                item_delivery.save()

        # CHECK IF ORDER HAS REORDERED ITEM
        self.mark_reordered(order)

        return order.get_billing_url()

    def mark_reordered(self, order):
        # 再注文商品があるかチェック
        has_reordered_item = False
        lst = [item.extra_info.get('reordered', False) for item in order.get_order_items()]
        if True in lst:
            has_reordered_item = True
        order.extra_info['has_reordered_item'] = has_reordered_item
        order.save()

    # def mark_mydesign(self, order):


@method_decorator(login_required, name='dispatch')
class CreateDeliveryAddressAPIView(APIView):
    """配送先の設定
    Jsonデータを受ける
    use_as_billing_addressの時は請求先も設定
    設定した住所をユーザーのデフォルトに
    """

    def post(self, request, format=None):
        order = Order.objects.get_current_order(request)
        form = DeliveryAddressCreationForm(request.data)

        # FORM VALIDATION
        if form.is_valid():
            name = form.cleaned_data['name']
            postal_code = form.cleaned_data['postal_code']
            prefecture = form.cleaned_data['prefecture']
            city = form.cleaned_data['city']
            building = form.cleaned_data['building']
            tel = form.cleaned_data['tel']

            # TODO: CHECK IF THERE IS THE SAME ADDRESS (DO NOT CREATE EVERYTIME)
            # DELIVERY ADDRESS CREATION
            da = DeliveryAddress.objects.create(
                user=request.user,
                name=name,
                postal_code=postal_code,
                prefecture=prefecture,
                city=city,
                building=building,
                tel=tel,
            )

            # SET AS DEFAULT ADDRESS
            request.user.change_default_delivery_address(da)

            # SET ORDER ADDRESS
            order_delivery = order.delivery_address
            order_delivery.name = name
            order_delivery.postal_code = postal_code
            order_delivery.prefecture = prefecture
            order_delivery.city = city
            order_delivery.building = building
            order_delivery.tel = tel
            order_delivery.save()

            use_as_billing_address = False

            # BILLING ADDRESS CREATION
            if form.cleaned_data['use_as_billing_address']:
                ba = BillingAddress.objects.create(
                    user=request.user,
                    name=name,
                    postal_code=postal_code,
                    prefecture=prefecture,
                    city=city,
                    building=building,
                    tel=tel,
                )
                request.user.change_default_billing_address(ba)

                # SET ORDER ADDRESS
                order_billing = order.billing_address
                order_billing.name = name
                order_billing.postal_code = postal_code
                order_billing.prefecture = prefecture
                order_billing.city = city
                order_billing.building = building
                order_billing.tel = tel
                order_billing.save()

                use_as_billing_address = True

            # SET ITEM DELIVERY ADDRESS
            for item in order.items.all():
                item_delivery = item.delivery
                item_delivery.address = da
                item_delivery.name = name
                item_delivery.postal_code = postal_code
                item_delivery.prefecture = prefecture
                item_delivery.city = city
                item_delivery.building = building
                item_delivery.tel = tel
                item_delivery.save()

            # RESPONSE DATA
            delivery_address = {
                "full_name": order_delivery.get_full_name(),
                "postal_code": order_delivery.postal_code,
                "prefecture": order_delivery.prefecture,
                "city": order_delivery.city,
                "building": order_delivery.building,
                "tel": order_delivery.tel,
            }
            return Response({"state": "success",
                             "delivery_address": delivery_address,
                             "use_as_billing_address": use_as_billing_address}, status=status.HTTP_200_OK)

        # RETURN MESSAGES FOR INVALID FIELDS
        return Response({'message': 'Form incomplete.',
                         'errors': dict(form.errors.items())}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(login_required, name='dispatch')
class CreateBillingAddressAPIView(APIView):
    """請求先の設定
    Jsonデータを受ける
    設定した住所をユーザーのデフォルトに
    """

    def post(self, request, format=None):
        order = Order.objects.get_current_order(request)
        form = BillingAddressCreationForm(request.data)
        if form.is_valid():
            name = form.cleaned_data['name']
            postal_code = form.cleaned_data['postal_code']
            prefecture = form.cleaned_data['prefecture']
            city = form.cleaned_data['city']
            building = form.cleaned_data['building']
            tel = form.cleaned_data['tel']

            # BILLING ADDRESS CREATION
            ba = BillingAddress.objects.create(
                user=request.user,
                name=name,
                postal_code=postal_code,
                prefecture=prefecture,
                city=city,
                building=building,
                tel=tel,
            )

            # SET AS DEFAULT ADDRESS
            request.user.change_default_billing_address(ba)

            # SET ORDER ADDRESS
            order_billing = order.billing_address
            order_billing.name = name
            order_billing.postal_code = postal_code
            order_billing.prefecture = prefecture
            order_billing.city = city
            order_billing.building = building
            order_billing.tel = tel
            order_billing.save()

            # RESPONSE DATA
            billing_address = {
                "name": order_billing.get_full_name(),
                "postal_code": order_billing.postal_code,
                "prefecture": order_billing.prefecture,
                "city": order_billing.city,
                "building": order_billing.building,
                "tel": order_billing.tel
            }
            return Response({"state": "success",
                             "billing_address": billing_address}, status=status.HTTP_200_OK)

        # RETURN MESSAGES FOR INVALID FIELDS
        return Response({'message': 'Form incomplete.',
                         'errors': dict(form.errors.items())}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(login_required, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class MakeChargeAPIView(APIView):
    """決済完了API
    決済はPayJP上で仮決済状態となる
    """

    # TODO: SAVE DATA ONCE
    @transaction.atomic
    def post(self, request, format=None):
        user = self.request.user
        order = Order.objects.get_current_order(self.request)

        # BLOCK NON_NEW ORDERS
        if order.state != 'new':
            return Response({'message': "Invalid order"}, status=status.HTTP_400_BAD_REQUEST)

        payment_method = request.data.get('payment_method')

        if payment_method == 'credit_card':
            # TODO: DO NOT USE PAYJP FUNCTION HERE
            c_id = user.payjpinfo.customer_id

            token = request.data.get('card', None)
            if token:
                card = payjp_has_card(c_id, token)
                if card:
                    payjp_change_default_card(c_id, card)
                else:
                    payjp_create_card(c_id, token)

            # PAY WITH DEFAULT CARD
            charge = payjp_create_charge_with_customer_id(c_id,
                                                          order.total,
                                                          order.ref_code)

            # TRANSACTION CREATION
            Transaction.objects.create(
                user=user,
                token=charge.id,
                order=order,
                amount=order.total,
                card=charge.card.id,
                type='credit_card',
            )
        elif payment_method == 'bank_transfer':
            # TRANSACTION CREATION
            # TODO: SET TOKEN HERE
            code = "".join(order.ref_code.split('-'))[:7]
            if not code.isdecimal():
                code = re.sub('[a-z]+', '', order.ref_code)[:7].zfill(7)

            Transaction.objects.create(
                user=user,
                token=code,
                order=order,
                amount=order.total,
                type='bank_transfer',
            )
        else:
            return Response({'message': 'Invalid payment method.'}, status=status.HTTP_400_BAD_REQUEST)

        # CHANGE STATE
        order.state = 'created'
        order.save()

        # USE SAME DESIGN WHEN ITEM IS REORDERED
        self.handle_reordered_item(order)

        # CHECK IF THERE IS ANY DESIGNLESS ITEM
        self.handle_item_without_design(order)

        capture_from_order(order)

        # RENEW CART
        cart = Cart.objects.get_from_request(self.request)
        cart.empty()

        # TODO: 銀行振り込みのときの文面
        # NOTIFICATIONS
        context = {
            'user': order.user,
            'order': order,
            'expiry_date': datetime.today() + timedelta(days=settings.PAYMENT_EXPIRY_DAYS)
        }
        send_notifications(order, '', context)

        # RETURN URL TO THE THANKYOU VIEW
        return Response({
            "message": "success",
            "redirect_to": "".join([reverse('thankyou'), '?', urlencode(dict(oid=order.ref_code))])
        }, status=status.HTTP_200_OK)

    def handle_reordered_item(self, order):
        for item in order.get_order_items():
            reordered = item.extra_info.get('reordered', False)
            from_ref_code = item.extra_info.get('reordered_from', '')
            from_item = OrderItem.objects.filter(ref_code=from_ref_code).first()
            if reordered and from_item:
                # if reordered
                design = item.design
                design.data = from_item.design.data
                design.state = 'confirmed'
                design.save()

    # def handle_mydesign_item(self, order):

    def handle_item_without_design(self, order):
        for item in order.get_order_items():
            is_design_necessary = item.product.info.is_design_necessary
            if not is_design_necessary:
                design = item.design
                design.state = 'confirmed'
                design.save()


@method_decorator(login_required, name='dispatch')
class ThankYouView(TemplateView):
    """決済完了画面の表
    """

    template_name = "billing/thankyou.html"

    def get(self, request, **kwargs):
        try:
            order = Order.objects.get(ref_code=request.GET.get("oid"))
            current_order = Order.objects.get_current_order(request)
            if order != current_order:
                return redirect('home')
        except ObjectDoesNotExist as e:
            return redirect('home')
        return super().get(request, **kwargs)


@method_decorator(login_required, name='dispatch')
class ThankYouAPIView(APIView):

    def get(self, request, format=None, **kwargs):
        order = Order.objects.filter(ref_code=kwargs.get("ref_code")).first()
        current_order = Order.objects.get_current_order(request)
        if order and order == current_order:
            data = OrderSerializer(order).data
            has_design_necessary_item = False
            for i in order.get_order_items():
                if not i.product.info.is_design_necessary or \
                    i.extra_info.get("reordered") or \
                    i.extra_info.get("from_mydesign"):
                    has_design_necessary_item = True
            data["has_design_necessary_item"] = has_design_necessary_item
            return Response(data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(login_required, name='dispatch')
class InstantBuyAPIView(APIView):
    """ 今すぐ買うの情報取得（価格、デフォルトカード、デフォルト住所）
    価格計算をして情報を返す
    """

    def post(self, request, format=None):
        data = request.data
        slug = data.get('product')
        product = Product.objects.filter(slug=slug).first()
        options = data.get('options')
        reordered = options.get('reordered', False)
        from_mydesign = options.get('from_mydesign', False)
        user = request.user
        if product and options:
            (unit_price, plate_price, mold_price, product_total, shipping_price, total_without_tax) = \
                product.get_prices(options, reordered, from_mydesign)
            tax = ceil(total_without_tax * settings.TAX_RATE)
            prices = {
                'unit_price': unit_price,
                'plate_price': plate_price,
                'mold_price': mold_price,
                'product_total': product_total,
                'shipping_price': shipping_price,
                'subtotal': total_without_tax,
                'tax': tax,
                'total': total_without_tax + tax,
            }
            _address = user.get_default_delivery_address()
            address = {
                "id": _address.id,
                "name": _address.name,
                "postal_code": _address.postal_code,
                "address": _address.get_full_address(),
            }

            return Response({
                "prices": prices,
                "address": address,
                "card": self._get_default_card_data(user),
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Invalid parameters.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def _get_default_card_data(self, user):
        c_id = user.payjpinfo.customer_id
        default_id = payjp_get_default_card(c_id)
        cards = payjp_get_customer_cards(c_id)
        card = {}
        for c in cards:
            if c['id'] == default_id:
                card = {
                    "name": c['name'],
                    "id": c['id'],
                    "brand": c['brand'],
                    "last4": c['last4'],
                    "exp_month": c['exp_month'],
                    "exp_year": c['exp_year']
                }
                break
        return card


@method_decorator(login_required, name='dispatch')
class InstantBuyChargeAPIView(APIView):
    """ 即買ボタン
    Orderを作成
    Transaction作成
    Designを引き継ぐ
    通知送信
    """

    @transaction.atomic
    def post(self, request, format=None):
        user = request.user
        data = request.data
        slug = data.get('product')
        product = Product.objects.filter(slug=slug).first()
        options = data.get('options')
        reordered = options.get('reordered', False)
        from_mydesign = options.get('from_mydesign', False)
        mydesign_id = options.get('mydesign_id')
        mydesign = MyDesign.objects.filter(user=user, id=mydesign_id).first()
        payment_method = data.get('payment_method')

        if not (product and options and mydesign and payment_method):
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        # PRICE RE-ESTIMATION
        (unit_price, plate_price, mold_price, product_total, shipping_price, total_without_tax) = \
            product.get_prices(options, reordered, from_mydesign)
        tax = ceil(total_without_tax * settings.TAX_RATE)

        ref_code = str(request.user.id) + '-' + '-'.join(str(datetime.now().timestamp()).split("."))
        default_delivery_address = request.user.get_default_delivery_address()
        stored_request = Order.objects.stored_request(request)

        # ORDER CREATION
        order = Order.objects.create(
            ref_code=ref_code,
            user=user,
            product_total=product_total,
            plate_total=plate_price,
            mold_total=mold_price,
            shipping_total=shipping_price,
            tax_total=tax,
            total=total_without_tax + tax,
            state="new",
            stored_request=stored_request,
        )

        # CREATE ORDER ADDRESSES
        # TODO: 請求先どうするか問題
        order_delivery = OrderDeliveryAddress.objects.create(order=order)
        order_billing = OrderBillingAddress.objects.create(order=order)
        order_delivery.name = default_delivery_address.name
        order_delivery.postal_code = default_delivery_address.postal_code
        order_delivery.prefecture = default_delivery_address.prefecture
        order_delivery.city = default_delivery_address.city
        order_delivery.building = default_delivery_address.building
        order_delivery.tel = default_delivery_address.tel
        order_delivery.save()
        order_billing.name = default_delivery_address.name
        order_billing.postal_code = default_delivery_address.postal_code
        order_billing.prefecture = default_delivery_address.prefecture
        order_billing.city = default_delivery_address.city
        order_billing.building = default_delivery_address.building
        order_billing.tel = default_delivery_address.tel
        order_billing.save()

        # CREATE ORDER ITEM
        prices = {
            'product_total': product_total,
            'plate_price': plate_price,
            'mold_price': mold_price,
            'unit_price': unit_price,
            'shipping_price': shipping_price,
            'subtotal': total_without_tax,
            'tax': tax,
            'total': total_without_tax + tax,
        }
        orderitem = OrderItem.objects.create(
            order=order,
            ref_code=ref_code + '-0001',
            product=product,
            product_name=product.name,
            product_slug=product.slug,
            quantity=options.get('quantity'),
            prices=prices,
            extra_info=options,
        )

        # CONFIRM DESIGN
        design = orderitem.design
        design.data = mydesign.design.data
        design.state = 'confirmed'
        design.save()

        # MAKE IT CURRENT ORDER
        Order.objects.set_current_order(self.request, ref_code)

        if payment_method == 'credit_card':
            # PAY WITH DEFAULT CARD
            c_id = user.payjpinfo.customer_id
            charge = payjp_create_charge_with_customer_id(c_id,
                                                          order.total,
                                                          order.ref_code)

            # TRANSACTION CREATION
            Transaction.objects.create(
                user=user,
                token=charge.id,
                order=order,
                amount=order.total,
                card=charge.card.id,
                type='credit_card',
            )
        elif payment_method == 'bank_transfer':
            code = "".join(order.ref_code.split('-'))[:7]
            if not code.isdecimal():
                code = re.sub('[a-z]+', '', order.ref_code)[:7].zfill(7)
            # TRANSACTION CREATION
            Transaction.objects.create(
                user=user,
                token=code,
                order=order,
                amount=order.total,
                type='bank_transfer',
            )
        else:
            return Response({'message': 'Invalid payment method.'}, status=status.HTTP_400_BAD_REQUEST)

        # CHANGE STATE
        order.state = 'created'
        order.save()
        mydesign.ordered_num += 1
        mydesign.save()

        capture_from_order(order)

        # NOTIFICATIONS
        context = {
            'user': order.user,
            'order': order,
            'expiry_date': datetime.today() + timedelta(days=settings.PAYMENT_EXPIRY_DAYS)
        }
        send_notifications(order, '', context)

        # RETURN URL TO THE THANKYOU VIEW
        return Response({
            "message": "success",
            "redirect_to": "".join([reverse('thankyou'), '?', urlencode(dict(oid=order.ref_code))])
        }, status=status.HTTP_200_OK)

