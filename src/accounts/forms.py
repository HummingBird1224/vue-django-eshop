from django import forms
from django.forms import ValidationError
from allauth.account.forms import SignupForm
from allauth.account.utils import setup_user_email
from .adapter import get_adapter
from .models import DeliveryAddress, BillingAddress
import re


class SignupForm(SignupForm):

    company_name = forms.CharField(max_length=255,
                                   required=False,
                                   widget=forms.TextInput(
                                       attrs={'autofocus': 'autofocus'}))

    url = forms.URLField(max_length=200,
                         required=False)

    name = forms.CharField(max_length=255,
                           widget=forms.TextInput(
                               attrs={'autofocus': 'autofocus'}))

    is_confirmed = forms.NullBooleanField(widget=forms.CheckboxInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_is_confirmed(self):
        is_confirmed = self.cleaned_data.get('is_confirmed')
        if not is_confirmed:
            raise ValidationError("プライバシーポリシーと利用規約の同意が必要です。")
        return is_confirmed

    def save(self, request):
        adapter = get_adapter(request)
        user = adapter.new_user(request)
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


class DeliveryAddressCreationForm(forms.ModelForm):

    class Meta:
        model = DeliveryAddress
        fields = ['user', 'name', 'postal_code', 'prefecture', 'city', 'tel']


class BillingAddressCreationForm(forms.ModelForm):

    class Meta:
        model = BillingAddress
        fields = ['user', 'name', 'postal_code', 'prefecture', 'city', 'tel']
