from django.urls import path
from .views import (BillingView,
                    ThankYouView,
                    CreateOrderRedirectView)

urlpatterns = [
    path('', BillingView.as_view(), name='billing'),
    path('create-order/', CreateOrderRedirectView.as_view(), name='create_order'),
    path('thankyou/', ThankYouView.as_view(), name='thankyou'),
]
