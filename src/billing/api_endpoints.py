from django.urls import path
from .views import (MakeChargeAPIView,
                    CreateDeliveryAddressAPIView,
                    CreateBillingAddressAPIView,
                    GetOrderInfoAPIView,
                    InstantBuyAPIView,
                    InstantBuyChargeAPIView,
                    ThankYouAPIView)

urlpatterns = [
    path('create-billing-address/', CreateBillingAddressAPIView.as_view(), name='create_billing_address'),
    path('create-delivery-address/', CreateDeliveryAddressAPIView.as_view(), name='create_delivery_address'),
    path('charge/', MakeChargeAPIView.as_view(), name='charge'),
    path('order-info/', GetOrderInfoAPIView.as_view(), name='api_order_info'),
    path('instantbuy/', InstantBuyAPIView.as_view(), name='instant_buy_api'),
    path('instantbuy/charge/', InstantBuyChargeAPIView.as_view(), name='instant_buy_charge_api'),
    path('thankyou/<str:ref_code>/', ThankYouAPIView.as_view(), name='thankyou_api'),
]
