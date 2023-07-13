from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import resolve_url
from allauth.utils import import_attribute
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import (user_username,
                                   user_email,
                                   user_field,
                                   get_next_redirect_url)
import json
from carts.models import Cart
from orders.models import Order


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        company_name = data.get('company_name')
        url = data.get('url')
        name = data.get('name')
        email = data.get('email')
        username = data.get('username')
        user_email(user, email)
        user_username(user, username)
        if company_name:
            user_field(user, 'company_name', company_name)
        if url:
            user_field(user, 'url', url)
        if name:
            user_field(user, 'name', name)
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        self.set_extra_info(request, user)
        if commit:
            user.save()
        return user

    def set_extra_info(self, request, user):
        extra_info = {}
        extra_info['campaign'] = request.session.get('external_service')
        setattr(user, 'extra_info', extra_info)
        return user

    def send_confirmation_mail(self, request, emailconfirmation, signup, redirect_to=None):
        current_site = get_current_site(request)
        activate_url = self.get_email_confirmation_url(
            request,
            emailconfirmation)
        ctx = {
            "user": emailconfirmation.email_address.user,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": emailconfirmation.key,
            "redirect_to": redirect_to,
        }
        if signup:
            email_template = 'account/email/email_confirmation_signup'
        else:
            email_template = 'account/email/email_confirmation'
        self.send_mail(email_template,
                       emailconfirmation.email_address.email,
                       ctx)

    def get_login_redirect_url(self, request):
        assert request.user.is_authenticated
        ret = get_next_redirect_url(request)
        if ret:
            return ret
        url = getattr(settings, "LOGIN_REDIRECT_URLNAME", None)
        if url:
            warnings.warn("LOGIN_REDIRECT_URLNAME is deprecated, simply"
                          " use LOGIN_REDIRECT_URL with a URL name",
                          DeprecationWarning)
        else:
            url = settings.LOGIN_REDIRECT_URL
        return resolve_url(url)


    def login(self, request, user):
        # DATA BEFORE LOGIN
        anonymous_cart = Cart.objects.get_from_request(self.request)
        anonymous_order = Order.objects.clear_order(self.request)
        # LOGIN ACTION OCCURS HERE WITH SESSION FLUSHING
        super().login(request, user)
        # AUTHENTICATED USER'S CART
        Cart.objects.clear_cart(self.request)
        authenticated_cart = Cart.objects.get_from_request(self.request)
        # MERGE CARTS
        if anonymous_cart and authenticated_cart and anonymous_cart != authenticated_cart:
            authenticated_cart.merge_with(anonymous_cart)
        # SET CURRENT ORDER
        if anonymous_order:
            Order.objects.set_current_order(self.request, anonymous_order)


def get_adapter(request=None):
    return import_attribute('accounts.adapter.CustomAccountAdapter')(request)
