from django.urls import path
from .views import (
    CaseStudyRetrieveAPIView,
    CaseStudyListAPIView,
    CaseStudyCategoryListAPIView,
    CaseStudyCategoryRetrieveAPIView,
    CaseStudySameTagListAPIView,
)

urlpatterns = [
    path('<str:category>/<str:tag>',
         CaseStudyListAPIView.as_view(), name='api_casestudy_list'),
    path('category/', CaseStudyCategoryListAPIView.as_view(),
         name='api_casestudy_category_list'),
    path('category/<slug:slug>/', CaseStudyCategoryRetrieveAPIView.as_view(),
         name='api_casestudy_category_search'),
    path('<slug:slug>/', CaseStudyRetrieveAPIView.as_view(),
         name='api_casestudy'),
    path('<str:category>/<str:tag>/<slug:slug>/', CaseStudySameTagListAPIView.as_view(),
         name='api_casestudy_tag_list'),
]
