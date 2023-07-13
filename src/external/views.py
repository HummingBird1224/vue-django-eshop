from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from products.models import Product, ProductCategory
from products.serializers import ProductSerializer
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView
from allauth.socialaccount.models import SocialAccount
from .provider import ColorMeProvider, BaseProvider
from .tasks import send_notifications
from math import ceil
import requests


User = get_user_model()


class ExternalServiceRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        redirect_to = self.request.GET.get('next')
        service_name = self.request.GET.get('from')
        if redirect_to and service_name:
            self.request.session['external_service'] = service_name
            return redirect_to
        return reverse('home')


#######################################################
# BASE (https://www.notion.so/BASE-STORES-5c915c6307b24156bed614571b3cbb6a)
#######################################################
class BaseLandingView(TemplateView):

    template_name = 'external/base_landing.html'


class BaseProductListAPIView(ListAPIView):
    """BASE商品のリストを返す
    """
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        cat = ProductCategory.objects.filter(slug='base').first()
        return Product.objects.filter(category=cat, is_active=True)


@method_decorator(csrf_protect, name='dispatch')
class BasePriceListAPIView(APIView):
    """商品の各ロット数での合計金額のリストを返す
    """
    permission_classes = (AllowAny,)

    def post(self, request, format=None, **kwargs):
        data = request.data
        slug = data.get('product')
        p = Product.objects.filter(slug=slug).first()
        if not p:
            return Response({'message': 'Product Does Not Exist.'}, status=status.HTTP_400_BAD_REQUEST)

        lot_list = []
        try:
            lots = p.options.get(slug='quantity')
            for v in lots.items.all():
                lot_list.append(v.value)
        except Exception as e:
            return Response({'message': 'Insufficient Product Data.'}, status=status.HTTP_400_BAD_REQUEST)
        vals = data.get('options')
        res = {}
        try:
            for q in lot_list:
                vals['quantity'] = q
                (_, _, _, product_total, _, _) = p.get_prices(vals)
                res[str(q)] = product_total
        except ValidationError:
            return Response({'message': 'Invalid Parameters.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'state': 'success', 'prices': res}, status=status.HTTP_200_OK)


@method_decorator(csrf_protect, name='dispatch')
class BaseEstimationAPIView(APIView):
    """見積もり
    """
    permission_classes = (AllowAny,)

    def post(self, request, format=None, **kwargs):
        data = request.data
        slug = data.get('product')
        p = Product.objects.filter(slug=slug).first()
        if not p:
            return Response({'message': 'Product Does Not Exist.'}, status=status.HTTP_400_BAD_REQUEST)
        vals = data.get('options')
        try:
            (unit_price, plate_price, mold_price, product_total, shipping_price, total_without_tax) = p.get_prices(vals)
            tax = ceil(total_without_tax * settings.TAX_RATE)
            res = {
                'unit_price': unit_price,
                'plate_price': plate_price,
                'mold_price': mold_price,
                'product_total': product_total,
                'shipping_price': shipping_price,
                'subtotal': total_without_tax,
                'tax': tax,
                'total': total_without_tax + tax,
            }
        except ValidationError:
            return Response({'message': 'Invalid Parameters.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'state': 'success', 'prices': res}, status=status.HTTP_200_OK)


class BaseAdapter(OAuth2Adapter):

    provider_id = BaseProvider.id
    # redirect_uri_protocol = 'https'
    supports_state = False
    access_token_url = 'https://api.thebase.in/1/oauth/token'
    authorize_url = 'https://api.thebase.in/1/oauth/authorize'
    profile_url = 'https://api.thebase.in/1/users/me'

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        login = self.get_provider().sociallogin_from_response(request, extra_data)
        return login


#######################################################
# FujiLogi
#######################################################
class FujiLogiLandingView(TemplateView):

    template_name = 'external/fujilogi_landing.html'


class FujiLogiProductListAPIView(ListAPIView):
    """フジロジテック商品のリストを返す
    """
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        cat = ProductCategory.objects.filter(slug='fujilogi').first()
        return Product.objects.filter(category=cat, is_active=True)


@method_decorator(csrf_protect, name='dispatch')
class FujiLogiPriceListAPIView(BasePriceListAPIView):
    """商品の各ロット数での合計金額のリストを返す
    """
    permission_classes = (AllowAny,)


@method_decorator(csrf_protect, name='dispatch')
class FujiLogiEstimationAPIView(BaseEstimationAPIView):
    """見積もり
    """
    permission_classes = (AllowAny,)


#######################################################
# Future Shop
#######################################################
class FutureShopLandingView(TemplateView):

    template_name = 'external/futureshop_landing.html'


class FutureShopProductListAPIView(ListAPIView):
    """COLORME商品のリストを返す
    """
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        cat = ProductCategory.objects.filter(slug='futureshop').first()
        return Product.objects.filter(category=cat, is_active=True)


@method_decorator(csrf_protect, name='dispatch')
class FutureShopPriceListAPIView(BasePriceListAPIView):
    """商品の各ロット数での合計金額のリストを返す
    """
    permission_classes = (AllowAny,)


@method_decorator(csrf_protect, name='dispatch')
class FutureShopEstimationAPIView(BaseEstimationAPIView):
    """見積もり
    """
    permission_classes = (AllowAny,)


#######################################################
# Color Me (https://www.notion.so/147c0c21a9a24c718af31960720b59f4)
#######################################################
class ColorMeLandingView(TemplateView):

    template_name = 'external/colorme_landing.html'


class ColorMeProductListAPIView(ListAPIView):
    """COLORME商品のリストを返す
    """
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        cat = ProductCategory.objects.filter(slug='colorme').first()
        return Product.objects.filter(category=cat, is_active=True)


@method_decorator(csrf_protect, name='dispatch')
class ColorMePriceListAPIView(BasePriceListAPIView):
    """商品の各ロット数での合計金額のリストを返す
    """
    permission_classes = (AllowAny,)


@method_decorator(csrf_protect, name='dispatch')
class ColorMeEstimationAPIView(BaseEstimationAPIView):
    """見積もり
    """
    permission_classes = (AllowAny,)


@method_decorator(require_POST, name='dispatch')
class ColorMeAppInstallAPI(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        send_notifications('colorme_app_install')
        sa = SocialAccount.objects.filter(uid=request.data['account_id']).first()

        if sa:
            user = sa.user
            user.is_active = True
            user.save()
        return Response({'redirect_url': 'https://canal.ink/external/colorme/'}, status=status.HTTP_200_OK)


@method_decorator(require_POST, name='dispatch')
class ColorMeAppUninstallAPI(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        send_notifications('colorme_app_uninstall')
        sa = SocialAccount.objects.filter(uid=request.data['account_id']).first()

        if sa:
            user = sa.user
            user.is_active = False
            user.save()
        return Response({}, status=status.HTTP_200_OK)


class ColorMeAdapter(OAuth2Adapter):

    provider_id = ColorMeProvider.id
    # redirect_uri_protocol = 'https'
    supports_state = False
    access_token_url = 'https://api.shop-pro.jp/oauth/token'
    authorize_url = 'https://api.shop-pro.jp/oauth/authorize'
    profile_url = 'https://api.shop-pro.jp/v1/shop.json'

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        login = self.get_provider().sociallogin_from_response(request, extra_data)
        return login


class RedirectOAuth2LoginView(OAuth2LoginView):
    def dispatch(self, request, *args, **kwargs):
        request.session['login_redirect_url'] = request.GET.get('login_redirect_url')
        return super().dispatch(request, *args, **kwargs)


colorme_oauth2_login = RedirectOAuth2LoginView.adapter_view(ColorMeAdapter)
colorme_oauth2_callback = OAuth2CallbackView.adapter_view(ColorMeAdapter)
base_oauth2_login = RedirectOAuth2LoginView.adapter_view(BaseAdapter)
base_oauth2_callback = OAuth2CallbackView.adapter_view(BaseAdapter)
