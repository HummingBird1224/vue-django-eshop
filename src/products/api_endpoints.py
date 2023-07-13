from django.urls import path
from .views import (
    ProductRetrieveAPIView,
    ProductEstimationAPIView,
    ProductListEtimationAPIView,
    CategoryListAPIView,
    CategoryRetrieveAPIView
)

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='api_category_list'),
    path('list/<slug:slug>/', CategoryRetrieveAPIView.as_view(), name='api_product_list'),
    path('<slug:slug>/', ProductRetrieveAPIView.as_view(), name='api_product'),
    path('<slug:slug>/estimate/', ProductEstimationAPIView.as_view(), name='api_product_estimate'),
    path('<slug:slug>/estimate/list/', ProductListEtimationAPIView.as_view(), name='api_product_estimate_list'),
]
