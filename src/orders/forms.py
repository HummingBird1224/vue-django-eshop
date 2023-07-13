from django import forms
from .models import ProvisionalOrderItemDesign


class UploadAIFileForm(forms.ModelForm):

    class Meta:
        model = ProvisionalOrderItemDesign
        fields = ['data', ]
