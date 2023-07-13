from django.urls import path
from django.conf.urls import url
from .views import (AccountUpdateView,
                    CustomLoginView,
                    CustomPasswordChangeView,
                    ConfirmEmailWithRedirectionView,
                    SignUpAPIView,
                    CreditManageView,
                    AddressManageView,
                    MyDesignView)


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/api/', SignUpAPIView.as_view(), name='signup_api'),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", ConfirmEmailWithRedirectionView.as_view(), name='account_confirm_email'),
    path("password/change/", CustomPasswordChangeView.as_view(), name="account_password_change"),
    path('update/', AccountUpdateView.as_view(), name='account_update'),
    path("credit/", CreditManageView.as_view(), name="account_credit_manage"),
    path("address/", AddressManageView.as_view(), name="account_address_manage"),
    path('mydesign/', MyDesignView.as_view(), name='mydesign'),
]
