from django import forms
from .models import CartItem


class FilmCartItemCreationForm(forms.ModelForm):

    color_num = forms.IntegerField(
        required=True,
    )

    width = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
    )

    height = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
    )

    depth = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
    )

    class Meta:
        model = CartItem
        fields = ['product',
                  'quantity',
                  'color_num',
                  'width',
                  'height',
                  'depth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].to_field_name = 'slug'
