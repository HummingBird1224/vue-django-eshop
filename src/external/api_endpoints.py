from django.urls import path
from .views import (
    BaseProductListAPIView,
    BasePriceListAPIView,
    BaseEstimationAPIView,
    ColorMeProductListAPIView,
    ColorMePriceListAPIView,
    ColorMeEstimationAPIView,
    ColorMeAppInstallAPI,
    ColorMeAppUninstallAPI,
    FujiLogiProductListAPIView,
    FujiLogiPriceListAPIView,
    FujiLogiEstimationAPIView,
    FutureShopProductListAPIView,
    FutureShopPriceListAPIView,
    FutureShopEstimationAPIView,
)

app_name = 'api:external'

urlpatterns = [
    # base
    path('base/products/', BaseProductListAPIView.as_view(), name='base_product_list'),
    path('base/products/pricelist/', BasePriceListAPIView.as_view(), name='base_price_list'),
    path('base/products/estimate/', BaseEstimationAPIView.as_view(), name='base_estimate'),
    # color me
    path('colorme/products/', ColorMeProductListAPIView.as_view(), name='colorme_product_list'),
    path('colorme/products/pricelist/', ColorMePriceListAPIView.as_view(), name='colorme_price_list'),
    path('colorme/products/estimate/', ColorMeEstimationAPIView.as_view(), name='colorme_estimate'),
    path('colorme/app/install/', ColorMeAppInstallAPI.as_view(), name='colorme_app_install'),
    path('colorme/app/uninstall/', ColorMeAppUninstallAPI.as_view(), name='colorme_app_uninstall'),
    # fujilogi
    path('fujilogi/products/', FujiLogiProductListAPIView.as_view(), name='fujilogi_product_list'),
    path('fujilogi/products/pricelist/', FujiLogiPriceListAPIView.as_view(), name='fujilogi_price_list'),
    path('fujilogi/products/estimate/', FujiLogiEstimationAPIView.as_view(), name='fujilogi_estimate'),
    # future shop
    path('futureshop/products/', FutureShopProductListAPIView.as_view(), name='futureshop_product_list'),
    path('futureshop/products/pricelist/', FutureShopPriceListAPIView.as_view(), name='futureshop_price_list'),
    path('futureshop/products/estimate/', FutureShopEstimationAPIView.as_view(), name='futureshop_estimate'),
]
