from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import (Product,
                     ProductInfo,
                     ProductPrice,
                     ProductImage,
                     ProductExampleImage,
                     ProductCategory,
                     ProductCategoryTag,
                     ProductUsecase,
                     ProductTag,
                     ProductOption,
                     ProductOptionItem,
                     ProductOptionCondition,
                     EasyDraft,
                     EasyDraftPrintArea)


class ImageInline(admin.TabularInline):

    model = None
    extra = 0
    readonly_fields = ('image_thumnail',)

    def image_thumnail(self, instance):
        return format_html(mark_safe('<img src="{}" height="100px"/>'.format(instance.image.url)))

    image_thumnail.short_description = "Image"


class ProductImageInline(ImageInline):

    model = ProductImage

class ProductExampleImageInline(ImageInline):

    model = ProductExampleImage

class ProductInfoInline(admin.StackedInline):

    model = ProductInfo


class ProductPriceInline(admin.StackedInline):

    model = ProductPrice


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'slug', 'parent_category', 'position', 'is_active']


@admin.register(ProductUsecase)
class ProductUsecaseAdmin(admin.ModelAdmin):

    model = ProductUsecase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', '__str__', 'slug', 'category', 'created_at', 'updated_at', 'is_active')
    ordering = ('-updated_at',)
    inlines = (ProductInfoInline, ProductPriceInline, ProductImageInline, ProductExampleImageInline)


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):

    pass


@admin.register(ProductCategoryTag)
class ProductTagAdmin(admin.ModelAdmin):

    list_display = ('name', 'position')
    ordering = ('-position',)


@admin.register(ProductOptionCondition)
class ProductOptionConditionAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'operator')


class ProductOptionItemInline(admin.StackedInline):

    model = ProductOptionItem


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):

    list_display = ('product', 'name', 'required', 'position', 'widget_type')
    inlines = (ProductOptionItemInline,)


class EasyDraftPrintAreaInline(admin.StackedInline):

    extra = 0
    model = EasyDraftPrintArea


@admin.register(EasyDraft)
class EasyDraftAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'slug')
    inlines = (EasyDraftPrintAreaInline,)

