from django import forms
from .models import NoticePost, NoticeCategory


class NoticePostModelForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        NoticeCategory.objects.filter(post_attachable=True),
        label='お知らせカテゴリ',
        empty_label='選択してください',
        to_field_name='pk',
    )

    class Meta:
        model = NoticePost
        fields = ('post_title', 'text', 'category')
