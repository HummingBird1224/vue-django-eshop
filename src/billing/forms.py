from django import forms
from django.forms import ValidationError
from accounts.models import DeliveryAddress, BillingAddress
import re


class DeliveryAddressCreationForm(forms.ModelForm):

    use_as_billing_address = forms.BooleanField(
        required=False
    )

    class Meta:
        model = DeliveryAddress
        fields = [
            'name',
            'postal_code',
            'prefecture',
            'city',
            'building',
            'tel',
            'use_as_billing_address',
        ]

    def clean_tel(self):
        _ = self.cleaned_data.get('tel')
        tel = re.sub("\\D", "", _)
        tel = tel.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
        if len(tel) not in [10, 11]:
            raise ValidationError("有効な電話番号を入力してください。")
        elif tel[0] != '0':
            raise ValidationError("有効な電話番号を入力してください。")
        elif tel[:2] == '00':
            raise ValidationError("有効な電話番号を入力してください。")
        return tel

    def clean_postal_code(self):
        _ = self.cleaned_data.get('postal_code')
        code = re.sub("\\D", "", _)
        code = code.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
        if len(code) != 7:
            raise ValidationError("有効な郵便番号を入力してください。")
        return code[:3] + '-' + code[3:]


class BillingAddressCreationForm(forms.ModelForm):

    class Meta:
        model = BillingAddress
        fields = [
            'name',
            'postal_code',
            'prefecture',
            'city',
            'building',
            'tel',
        ]

    def clean_tel(self):
        _ = self.cleaned_data.get('tel')
        tel = re.sub("\\D", "", _)
        tel = tel.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
        if len(tel) not in [10, 11]:
            raise ValidationError("有効な電話番号を入力してください。")
        elif tel[0] != '0':
            raise ValidationError("有効な電話番号を入力してください。")
        elif tel[:2] == '00':
            raise ValidationError("有効な電話番号を入力してください。")
        return tel

    def clean_postal_code(self):
        _ = self.cleaned_data.get('postal_code')
        code = re.sub("\\D", "", _)
        code = code.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
        if len(code) != 7:
            raise ValidationError("有効な郵便番号を入力してください。")
        return code[:3] + '-' + code[3:]
