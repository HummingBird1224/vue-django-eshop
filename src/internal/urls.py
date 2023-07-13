from django.urls import path
from .views import (
    InternalOrderListView,
    InternalOrderItemDetailView,
    InternalCreateCustomProductView,
    OrderItemStateLogCsvAPIView,
    DataAnalyticsView,
    CompleteBankTransferAPI,
    UncompleteBankTransferAPI,
    InternalNoticePostListView,
    InternalNoticePostDetailView,
    InternalNoticePostCreateView,
    ProductCreateView,
)
from django.views.generic import RedirectView

app_name = 'internal'
urlpatterns = [
    path('', RedirectView.as_view(url='/internal/orders/'), name='internal_redirect'),
    path('orders/', InternalOrderListView.as_view(), name='order_list'),
    path('orders/log/', OrderItemStateLogCsvAPIView.as_view(), name='order_item_update_log'),
    path('orders/<str:ref_code>/', InternalOrderItemDetailView.as_view(), name='order_detail'),
    path('orders/<str:ref_code>/banktransfer/complete/', CompleteBankTransferAPI.as_view(), name='order_bank_transfer_complete'),
    path('orders/<str:ref_code>/banktransfer/uncomplete/', UncompleteBankTransferAPI.as_view(), name='order_bank_transfer_uncomplete'),
    path('custom_product/create/', InternalCreateCustomProductView.as_view(), name='create_custom_product'),
    path('analytics/', DataAnalyticsView.as_view(), name='analytics'),
    path('notices/', InternalNoticePostListView.as_view(), name='notice_post_list'),
    path('notices/<int:pk>/', InternalNoticePostDetailView.as_view(), name='notice_post_detail'),
    path('notices/new', InternalNoticePostCreateView.as_view(), name='notice_post_create'),
    path('products/create/', ProductCreateView.as_view(), name='product-create')
]
