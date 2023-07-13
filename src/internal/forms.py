from django import forms
from notices.models import NoticeCategory
from orders.models import OrderItemDesign
from products.models import ProductCategory, ProductTag
from django.core.validators import FileExtensionValidator


class OrderItemForm(forms.Form):
    company = forms.CharField(
        label="発注先の印刷会社",
        max_length=200,
        required=False
    )

    tracking_code = forms.CharField(
        label="配達トラッキングコード",
        max_length=200,
        required=False
    )

    no_tracking_code = forms.BooleanField(
        label="自社配送",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'check'})
    )

    shipping_date = forms.DateTimeField(
        label="発送日",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )

    delivery_date = forms.DateTimeField(
        label="お届け日",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )

    state = forms.ChoiceField(
        required=True,
        choices=[(i, i) for i in range(9)],
    )

    comment = forms.CharField(
        label="コメント",
        required=False,
        widget=forms.Textarea
    )

    data = forms.FileField(
        label="コメント",
        required=False,
        widget=forms.FileInput,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'ai'])]
    )


class OrderItemCancelForm(forms.Form):
    pass
