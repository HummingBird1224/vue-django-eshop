from rest_framework import serializers
from .models import Order, OrderDeliveryAddress, OrderItem, OrderItemDesign, OrderItemDelivery
from products.serializers import EasyDraftSerializer
from utils.payjp_functions import *


class OrderItemDesignSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItemDesign
        fields = ['state',
                  'data']


class OrderItemDeliverySerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = OrderItemDelivery
        fields = ['state',
                  'full_name',
                  'postal_code',
                  'prefecture',
                  'city',
                  'building',
                  'tel',
                  'shipping_date',
                  'delivery_date',
                  'company',
                  'tracking_code']

    def get_full_name(self, instance):
        return instance.get_full_name()


class OrderItemSerializer(serializers.ModelSerializer):

    design = OrderItemDesignSerializer()
    delivery = OrderItemDeliverySerializer()
    is_easy_draft_available = serializers.SerializerMethodField()
    extra_info_str = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    is_reorderable = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['ref_code',
                  'product_name',
                  'product_image',
                  'link',
                  'quantity',
                  'extra_info',
                  'extra_info_str',
                  'size',
                  'unit_price',
                  'total',
                  'prices',
                  'design',
                  'delivery',
                  'state',
                  'is_reorderable',
                  'is_easy_draft_available']

    def get_is_easy_draft_available(self, instance):
        if instance.product.info.is_easy_draft_available:
            # 一時的に印刷面数が２の時はカンタン入稿なし
            # print_area_num = instance.extra_info.get('print_area_num', False)
            # if print_area_num and print_area_num != 1:
            #     return False
            return instance.product.info.is_easy_draft_available
        return False

    def get_extra_info_str(self, instance):
        return instance.render_extra_info()

    def get_size(self, instance):
        return instance.size_str

    def get_link(self, instance):
        return instance.product.get_absolute_url()

    def get_is_reorderable(self, instance):
        return instance.is_reorderable()

    def get_product_image(self, instance):
        return instance.product.get_thumbnail_url()


class OrderDeliverySerializer(serializers.ModelSerializer):

    full_address = serializers.SerializerMethodField()

    class Meta:
        model = OrderDeliveryAddress
        fields = ['name',
                  'full_address',
                  'postal_code',
                  'prefecture',
                  'city',
                  'building',
                  'tel']

    def get_full_address(self, instance):
        return instance.get_full_address()


class OrderWithoutCardInfoSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)
    prices = serializers.SerializerMethodField()
    delivery_address = OrderDeliverySerializer()
    transaction = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['user',
                  'state',
                  'ref_code',
                  'items',
                  'prices',
                  'delivery_address',
                  'currency',
                  'transaction',
                  'created_at']

    def get_prices(self, instance):
        return {
            "tax": instance.tax_total,
            "total": instance.total,
            "mold_price": instance.mold_total,
            "plate_price": instance.plate_total,
            "product_total": instance.product_total,
            "shipping_price": instance.shipping_total
        }

    def get_transaction(self, instance):
        t = instance.get_transaction()
        res = {
            "type": t.type,
            "is_captured": t.is_captured,
        }
        return res


class OrderSerializer(OrderWithoutCardInfoSerializer):

    def get_transaction(self, instance):
        t = instance.get_transaction()
        res = {
            "type": t.type,
            "is_captured": t.is_captured,
        }
        if t.type == 'credit_card':
            card = payjp_get_card_info(t.token)
            res['card'] = {
                "last4": card.last4,
                "exp_month": card.exp_month,
                "exp_year": card.exp_year,
                "brand": card.brand,
            }
        return res


class OrderItemForEasyDraftSerializer(serializers.ModelSerializer):

    design = OrderItemDesignSerializer()
    is_easy_draft_available = serializers.SerializerMethodField()
    easy_draft = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['ref_code',
                  'product_name',
                  'extra_info',
                  'design',
                  'is_easy_draft_available',
                  'easy_draft']

    def get_is_easy_draft_available(self, instance):
        if instance.product.info.is_easy_draft_available:
            # 一時的に印刷面数が２の時はカンタン入稿なし
            # print_area_num = instance.extra_info.get('print_area_num', False)
            # if print_area_num and print_area_num != 1:
            #     return False
            return instance.product.info.is_easy_draft_available
        return False

    def get_easy_draft(self, instance):
        easy_draft = instance.product.easydrafts
        if easy_draft:
            size = instance.extra_info.get('size', [])
            design_num = instance.extra_info.get('design_num')
            print_area_num = instance.extra_info.get('print_area_num', '1')
            if {'height', 'width', 'depth'}.issubset(size.keys()):
                ed_obj = easy_draft.filter(slug="{}_{}_{}_{}".format(str(size['height']),
                                                                     str(size['width']),
                                                                     str(size['depth']),
                                                                     str(print_area_num))).first()
            elif {'height', 'width'}.issubset(size.keys()):
                ed_obj = easy_draft.filter(slug="{}_{}_{}".format(str(size['height']),
                                                                  str(size['width']),
                                                                  str(print_area_num))).first()
            if ed_obj:
                return EasyDraftSerializer(ed_obj).data
        return None
