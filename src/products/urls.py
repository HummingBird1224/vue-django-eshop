from django.urls import path
from .views import (
    ProductDetailView,
    ProductListView,
)
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/catalog/flatbag/"), name="catalog_redirect"),
    path("<slug:slug>/", ProductListView.as_view(), name="catalog"),
    path("<slug:c_slug>/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
]
