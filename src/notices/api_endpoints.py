from django.urls import path
from .views import (
    NoticeListAPIView,
    NoticeReadAPIView,
    NoticePostDetailAPIView,
)

urlpatterns = [
    path('', NoticeListAPIView.as_view(), name='api_notices'),
    path('<int:pk>/', NoticePostDetailAPIView.as_view(), name='notice_post'),
    path('read/', NoticeReadAPIView.as_view(), name='api_notice_read'),
]
