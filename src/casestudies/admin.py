from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.text import format_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q, F

from .models import CaseStudy, CaseStudyCategory, CaseStudyImage

# Monkey patch admin to include the display decorator (available in future Django versions)
if not hasattr(admin, "display"):
    def display(description):
        def decorator(fn):
            fn.short_description = description
            return fn
        return decorator
    setattr(admin, "display", display)        

def get_children(parent, query):
    # query=query | Q(**{f"category": parent })
    childs=CaseStudyCategory.objects.filter(category=parent)

    for child in childs:
        query=query | Q(**{f"category": child })
        get_children(child, query)
    return query
        

class ImageInline(admin.TabularInline):

    model = None
    extra = 0
    readonly_fields = ('image_thumnail',)

    def image_thumnail(self, instance):
        return format_html(mark_safe('<img src="{}" height="100px"/>'.format(instance.image.url)))

    image_thumnail.short_description = "Image"


class CaseStudyImageInline(ImageInline):

    model = CaseStudyImage

class CaseStudyForm(forms.ModelForm):
    class Meta:
        model = CaseStudy
        fields = ['product', 'title', 'client', 'slug', 'text','text_url', 'product_category',
                  'shape', 'printing_method', 'material', 'usage', 'processing',
                  'sustainability', 'position', 'is_active']



@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):

    list_display = ['product', 'title', 'client', 'is_active']

    form = CaseStudyForm

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        db = kwargs.get('using')

        # if db_field.name == 'shape':
            # kwargs['widget'] = FilteredSelectMultiple(
            #     db_field.verbose_name,
            #     is_stacked=False
        #     # )
        if(db_field.name):
            field_name=db_field.name
            parent= get_object_or_404(CaseStudyCategory, slug=field_name)
            # query=Q(**{f"slug": field_name})
            query=Q(**{f"category": parent})
            query=get_children(parent, query)
            queryset=CaseStudyCategory.objects.filter(query)            
        else:
            return super().formfield_for_manytomany(db_field, request, **kwargs)

        # if 'queryset' not in kwargs:
        #     queryset = CaseStudy.objects.filter(is_active=True)
        #     if queryset is not None:
        kwargs['queryset'] = queryset

        form_field = db_field.formfield(**kwargs)
        msg = 'Hold down .'
        help_text = form_field.help_text
        form_field.help_text = (
            format_lazy('{} {}', help_text, msg) if help_text else msg
        )
        return form_field
    inlines = [CaseStudyImageInline]


class CaseStudyCategoryForm(forms.ModelForm):
    class Meta:
        model = CaseStudy
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CaseStudyCategoryForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset=CaseStudyCategory.objects.exclude(category=None)


@admin.register(CaseStudyCategory)
class CaseStudyCategoryAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'slug', 'category', 'position', 'is_active']
    # form = CaseStudyCategoryForm

