from django.urls import path
from .views import NoticeListView, NoticePostDetailView

urlpatterns = [
    path('', NoticeListView.as_view(), name='notices'),
    path('<int:pk>/', NoticePostDetailView.as_view(), name='notice_post')
]
