"""canal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('canal-admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('canal-api-auth/', include('rest_framework.urls')),
    # static pages
    path('', TemplateView.as_view(template_name="core/home.html"), name='home'),
    path('terms/', TemplateView.as_view(template_name="core/terms.html"), name='terms'),
    path('privacypolicy/', TemplateView.as_view(template_name="core/privacypolicy.html"), name='privacypolicy'),
    path('tokutei/', TemplateView.as_view(template_name='core/specified_commercial_transactions_act.html'), name='tokutei'),
    path('aboutus/', TemplateView.as_view(template_name="core/aboutus.html"), name='aboutus'),
    path('contact/complete/', TemplateView.as_view(template_name="core/contact_complete.html"), name='contact_complete'),
    path('document/request/complete/', TemplateView.as_view(template_name="core/document_request_complete.html"), name='document_request_complete'),
    # casestudies 
    path('casestudies/', include('casestudies.urls')),
    # products
    path('catalog/', include('products.urls')),
    # cart
    path('cart/', include('carts.urls')),
    # billing
    path('billing/', include('billing.urls')),
    # orders
    path('orders/', include('orders.urls')),
    # internal
    path('internal/', include('internal.urls')),
    # external
    path('external/', include('external.urls')),
    # notice
    path('notices/', include('notices.urls')),
    # internal
    path('api/internal/', include('internal.api_endpoints')),

    # API
    # TODO: APIとHTMLレスポンスの切り分け
    # accounts
    path('api/accounts/', include('accounts.api_endpoints')),
    # mydesign (url注意)
    path('api/accounts/', include('mydesign.api_endpoints')),
    # products
    path('api/products/', include('products.api_endpoints')),
    # cart
    path('api/cart/', include('carts.api_endpoints')),
    # orders
    path('api/orders/', include('orders.api_endpoints')),
    # billing
    path('api/billing/', include('billing.api_endpoints')),
    # external
    path('api/external/', include('external.api_endpoints')),
    # notices
    path('api/notices/', include('notices.api_endpoints')),
    # internal
    path('api/internal/', include('internal.api_endpoints')),
        # casestudies
    path('api/case_studies/', include('casestudies.api_endpoints')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

