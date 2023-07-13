from django.conf import settings
from rest_framework import serializers
from .models import (
    CaseStudy,
    CaseStudyCategory,
    CaseStudyImage
)
import re


comp_image = re.compile('"image": "img')
comp_design = re.compile('"data": "design_templates')


class CaseStudyCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseStudyCategory
        fields = ['id', 'name', 'slug', 'category', 'overview',
                  'text', 'image', 'URL', 'position', 'icon', 'advantage', 'disadvantage', 'explanatory_image']


class CaseStudySerializer(serializers.ModelSerializer):
    material = CaseStudyCategorySerializer(many=True)
    printing_method = CaseStudyCategorySerializer(many=True)
    shape = CaseStudyCategorySerializer(many=True)
    usage = CaseStudyCategorySerializer(many=True)
    processing = CaseStudyCategorySerializer(many=True)
    sustainability = CaseStudyCategorySerializer(many=True)
    product_category = CaseStudyCategorySerializer(many=True)
    images = serializers.SerializerMethodField()
    hover_image = serializers.SerializerMethodField()

    class Meta:
        model = CaseStudy
        fields = [
            'title', 'client', 'slug', 'text', 'images', 'product_category', 'shape', 'printing_method',
            'material', 'usage', 'processing', 'sustainability', 'position','hover_image', 'text_url'
        ]
    def get_images(self, instance):
        return instance.get_image_url_list()
    
    def get_hover_image(self, instance):
        return instance.get_hover_image_url()


class CaseStudyCategoryWithChildrenSerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CaseStudyCategory
        fields = ['name', 'slug', 'category', 'overview', 'text',
                  'image', 'URL', 'position', 'icon', 'children']

    def get_children(self, obj):
        """ self referral field """
        serializer = CaseStudyCategorySerializer(
            instance=CaseStudyCategory.objects.public().filter(category=obj),
            many=True
        )
        return serializer.data
