from django import template
from django.conf import settings
from django.urls import resolve
from carts.models import Cart

register = template.Library()


@register.filter()
def header_remove_path(request):
    url_names = [
        'product_estimate',
        'login',
        'account_signup',
        'billing',
        'product_estimate',

        'billing_markup',
        'estimate_markup',
        'estimate_under_markup',
        'estimate_vue_markup',
    ]
    return resolve(request.path).url_name in url_names


@register.filter()
def footer_remove_path(request):
    url_names = [
        'product_estimate',
        'login',
        'account_signup',
        'billing',
        'product_estimate',

        'billing_markup',
        'billing_complete_markup',
        'estimate_markup',
        'estimate_under_markup',
        'estimate_vue_markup',
    ]
    return resolve(request.path).url_name in url_names


@register.simple_tag
def static_url():
    return settings.STATIC_URL


@register.simple_tag(takes_context=True)
def cart_num_items(context):
    request = context['request']
    cart = Cart.objects.get_or_create_from_request(request)
    return cart.num_items


@register.filter()
def key(d, key_name):
    try:
        value = d[key_name]
    except KeyError:
        from django.conf import settings

        value = settings.TEMPLATE_STRING_IF_INVALID
    return value