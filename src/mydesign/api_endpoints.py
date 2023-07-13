from django.urls import path
from .views import (
    MyDesignListAPIView,
    MyDesignRenameAPIView,
    MyDesignReorderRetrieveAPIView,
)

urlpatterns = [
    path('mydesign/', MyDesignListAPIView.as_view(), name='mydesign_list_api'),
    path('mydesign/<int:id>/rename/', MyDesignRenameAPIView.as_view(), name='mydesign_rename_api'),
    path('mydesign/<int:id>/reorder/', MyDesignReorderRetrieveAPIView.as_view(), name='mydesign_reorder_api'),
]
