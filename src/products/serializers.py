from django.conf import settings
from rest_framework import serializers
from .models import (
    Product,
    ProductInfo,
    ProductCategory,
    ProductUsecase,
    ProductOption,
    ProductOptionItem,
    ProductOptionCondition,
    EasyDraft,
    EasyDraftPrintArea,
)
import re


comp_image = re.compile('"image": "img')
comp_design = re.compile('"data": "design_templates')


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ['name', 'slug', 'icon', 'detail', 'extra_info']


class ProductCategoryWithChildrenSerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProductCategory
        fields = ['name', 'slug', 'icon', 'detail', 'extra_info', 'children']

    def get_children(self, obj):
        """ self referral field """
        serializer = ProductCategorySerializer(
            instance=ProductCategory.objects.public().filter(parent_category=obj),
            many=True
        )
        return serializer.data


class EasyDraftPrintAreaSerializer(serializers.ModelSerializer):

    position = serializers.SerializerMethodField()

    class Meta:
        model = EasyDraftPrintArea
        fields = ['area_id', 'name', 'position', 'is_printable', 'image']

    def get_position(self, instance):
        if instance.is_printable:
            data = {}
            data["pdf"] = {
                "end": {"x": instance.pdf_pos_end_x, "y": instance.pdf_pos_end_y},
                "start": {"x": instance.pdf_pos_start_x, "y": instance.pdf_pos_start_y}
            }
            data["image"] = {
                "end": {"x": instance.image_pos_end_x, "y": instance.image_pos_end_y},
                "start": {"x": instance.image_pos_start_x, "y": instance.image_pos_start_y}
            }
            return data
        return


class EasyDraftSerializer(serializers.ModelSerializer):

    print_area = serializers.SerializerMethodField(read_only=True)
    pdf_size = serializers.SerializerMethodField()
    image_size = serializers.SerializerMethodField()
    pdf_color = serializers.SerializerMethodField()

    class Meta:
        model = EasyDraft
        fields = ['slug', 'print_area', 'pdf_size', 'image_size', 'pdf_color']

    def get_print_area(self, obj):
        serializer = EasyDraftPrintAreaSerializer(
            instance=EasyDraftPrintArea.objects.filter(easydraft=obj),
            many=True
        )
        return serializer.data

    def get_pdf_size(self, instance):
        return {'width': instance.pdf_width, 'height': instance.pdf_height}

    def get_image_size(self, instance):
        return {'width': instance.image_width, 'height': instance.image_height}

    def get_pdf_color(self, instance):
        return {'background': "#" + instance.pdf_background_color, 'border':  "#" + instance.pdf_border_color}


class ProductUsecaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductUsecase
        fields = ['name', 'slug', 'icon']


class ProductInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInfo
        exclude = ['id', 'product']


class ProductOptionConditionSerializer(serializers.ModelSerializer):

    option = serializers.SerializerMethodField()
    values = serializers.SerializerMethodField()

    class Meta:
        model = ProductOptionCondition
        exclude = ['id', 'item',]

    def get_option(self, instance):
        return instance.option.slug

    def get_values(self, instance):
        vals = []
        for val in instance.values.all():
            vals.append(val.value)
        return vals


class ProductOptionItemSerializer(serializers.ModelSerializer):

    condition = ProductOptionConditionSerializer(many=True, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = ProductOptionItem
        exclude = ['id', 'option']

    def get_data(self, instance):
        if instance.option.slug == 'size':
            prod = instance.option.product
            cat = prod.category.get_parent_or_self().slug
            zip_products = ["folding-carton","atype-fullcolor-small-lot"]
            format = ".zip" if prod.slug in zip_products else ".ai"
            return "design_templates/" + cat + "/" + prod.slug + "/" + instance.name + format
        return None


class ProductOptionSerializer(serializers.ModelSerializer):

    items = serializers.SerializerMethodField()

    class Meta:
        model = ProductOption
        fields = ['slug', 'name', 'detail', 'required', 'position', 'widget_type', 'modal_blocks', 'items', 'image']

    def get_items(self, instance):
        data = []
        for item in instance.items.filter(is_active=True):
            data.append(ProductOptionItemSerializer(item).data)
        return data


class ProductSerializer(serializers.ModelSerializer):

    category = ProductCategorySerializer(read_only=True)
    usecase = ProductUsecaseSerializer(many=True, read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    main_category = serializers.SerializerMethodField()
    info = ProductInfoSerializer(read_only=True)
    thumbnail = serializers.CharField(source='get_thumbnail_url', read_only=True)
    images = serializers.SerializerMethodField()
    example_images = serializers.SerializerMethodField()
    example_urls = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()
    easy_draft = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'category',
            'main_category',
            'usecase',
            'tags',
            'overview',
            'unit',
            'info',
            'thumbnail',
            'images',
            'example_images',
            'example_urls',
            'options',
            'easy_draft',
        ]
        read_only_fields = []

    def get_images(self, instance):
        return instance.get_image_url_list()

    def get_example_images(self, instance):
        return instance.get_example_image_url_list()

    def get_example_urls(self, instance):
        return instance.get_example_url_list()

    def get_main_category(self, instance):
        main_cat = instance.category.get_parent_or_self()
        return ProductCategorySerializer(main_cat).data

    def get_options(self, instance):
        data = []
        for option in instance.options.all():
            data.append(ProductOptionSerializer(option).data)
        return data

    def get_easy_draft(self, instance):
        data = {}
        for draft in instance.easydrafts.all():
            data[draft.slug] = EasyDraftSerializer(draft).data
        return data
