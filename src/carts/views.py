from django.conf import settings
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.views.generic.base import TemplateView, RedirectView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from products.models import Product
from .models import Cart, CartItem
from .serializers import CartSerializer
import json
from math import ceil
import logging


logger = logging.getLogger(__name__)


class CartView(TemplateView):
    """カート画面
    """

    template_name = "carts/cart.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart = Cart.objects.get_or_create_from_request(self.request)
        context['cart'] = cart
        return context


@method_decorator(csrf_protect, name='dispatch')
class AddToCartAPIView(APIView):
    """カートに商品追加API
    明示的にcsrf protection
    TODO: レスポンス内にバリデーション結果入れる
    """

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        cart = Cart.objects.get_or_create_from_request(request)
        data = request.data
        slug = data.get('product')
        product = Product.objects.filter(slug=slug).first()
        options = data.get('options')
        # 再注文とマイデザイン経由かのフラグ
        reordered = options.get('reordered', False)
        from_mydesign = options.get('from_mydesign', False)

        if product and options:
            try:
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
                CartItem.objects.create(
                    cart=cart,
                    product=product,
                    quantity=int(options['quantity']),
                    prices=prices,
                    extra_info=options,
                )
                cart.update()
                return Response({
                    'message': 'Added to cart.'
                }, status=status.HTTP_200_OK)
            except ValidationError as e:
                logger.error(e)
                Response({
                    'message': 'Invalid request.'
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'message': 'Invalid parameters.'
        }, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_protect, name='dispatch')
class DeleteFromCartAPIView(APIView):
    """カートから商品削除API
    明示的にcsrf protection
    レスポンス内に削除後の価格
    """

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        cart = Cart.objects.get_or_create_from_request(request)
        data = json.loads(request.body)
        item = CartItem.objects.filter(id=data.get("item_id")).first()
        if item and item.cart == cart:
            item.delete()
            cart.update()
            return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)
        return Response({
            "message": "Something wrong."
        }, status=status.HTTP_400_BAD_REQUEST)


class CartRetrieveAPIView(RetrieveAPIView):

    serializer_class = CartSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        return Cart.objects.get_or_create_from_request(self.request)
