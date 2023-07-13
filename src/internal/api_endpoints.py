from django.urls import path
from .views import ProductCreateAPIView, ProductCategoryAndTagListAPIView, AddCustomProductAPIView, CustomProductFormAPIView, NoticePOSTListAPIView


app_name = 'internal.api'
urlpatterns = [
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('products/create/cat-n-tag-list/', ProductCategoryAndTagListAPIView.as_view(), name='product_create_cat_n_tag_list'),
    path('custom-product/', CustomProductFormAPIView.as_view(), name='custom_product_form_data'),
    path('custom-product/add/', AddCustomProductAPIView.as_view(), name='add_custom_product'),
    path('notices/', NoticePOSTListAPIView.as_view(), name='notice_post_list'),
]
