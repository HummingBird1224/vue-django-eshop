from django.urls import path
from .views import (
    ExternalServiceRedirectView,
    BaseLandingView,
    ColorMeLandingView,
    FujiLogiLandingView,
    FutureShopLandingView,

    base_oauth2_login,
    base_oauth2_callback,
    colorme_oauth2_login,
    colorme_oauth2_callback,
)

from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import ColorMeProvider, BaseProvider

app_name = 'external'

urlpatterns = [
    path('redirect/', ExternalServiceRedirectView.as_view(), name='external_redirect'),
    path('base/', BaseLandingView.as_view(), name='base_landing'),
    path('colorme/', ColorMeLandingView.as_view(), name='colorme_landing'),
    path('fujilogi/', FujiLogiLandingView.as_view(), name='fujilogi_landing'),
    path('futureshop/', FutureShopLandingView.as_view(), name='futureshop_landing'),

    # Base Login
    path('base/login/', base_oauth2_login, name='base_login'),
    path('base/login/callback/', base_oauth2_callback, name='base_callback'),
    # Color me Login
    path('colorme/login/', colorme_oauth2_login, name='colorme_login'),
    path('colorme/login/callback/', colorme_oauth2_callback, name='colorme_callback'),
]
