from django.urls import path
from .views import (AccountCreditListAPIView,
                    AccountCreditCreateAPIView,
                    AccountCreditDeleteAPIView,
                    AccountCreditChangeDefaultAPIView,
                    AccountAddressListAPIView,
                    AccountAddressCreateAPIView,
                    AccountAddressDeleteAPIView,
                    AccountAddressChangeDefaultAPIView)

urlpatterns = [
    path('credit/', AccountCreditListAPIView.as_view(), name='api_credit'),
    path('credit/create/', AccountCreditCreateAPIView.as_view(), name='api_credit_create'),
    path('credit/delete/', AccountCreditDeleteAPIView.as_view(), name='api_credit_delete'),
    path('credit/change/', AccountCreditChangeDefaultAPIView.as_view(), name='api_credit_change'),

    path('address/', AccountAddressListAPIView.as_view(), name='api_address'),
    path('address/create/', AccountAddressCreateAPIView.as_view(), name='api_address_create'),
    path('address/delete/', AccountAddressDeleteAPIView.as_view(), name='api_address_delete'),
    path('address/change/', AccountAddressChangeDefaultAPIView.as_view(), name='api_address_change'),
]
