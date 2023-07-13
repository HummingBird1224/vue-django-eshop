from django.urls import path
from .views import (
    AddToCartAPIView,
    DeleteFromCartAPIView,
    CartRetrieveAPIView,
)

urlpatterns = [
    path('', CartRetrieveAPIView.as_view(), name='api_retrieve_cart'),
    path('add/', AddToCartAPIView.as_view(), name='api_add_to_cart'),
    path('delete/', DeleteFromCartAPIView.as_view(), name='delete_from_cart'),
]
