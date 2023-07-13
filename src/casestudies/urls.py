from django.urls import path
from .views import (
    CaseStudyList1View,
    CaseStudyCategoryView,
    CaseStudyCategoryTagView,
    CaseStudyDetailView,
)
from django.views.generic import RedirectView

urlpatterns = [
    path("", CaseStudyList1View.as_view(), name="casestudy_list"),
    # path("<str:category>/", CaseStudyCategoryView.as_view(), name="casestudy_category_list"),
    path("<str:category>/<str:tag>/", CaseStudyCategoryTagView.as_view(), name="casestudy_category_list"),
    path("<str:category>/<str:tag>/<slug:slug>", CaseStudyDetailView.as_view(), name="casestudy_detail"),
]
