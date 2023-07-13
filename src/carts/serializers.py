from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):

    size_str = serializers.SerializerMethodField()
    prices = serializers.SerializerMethodField()
    extra_info_str = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()
    product_url = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        exclude = ['product', 'cart', 'extra_info', 'created_at', 'in_cart']

    def get_size_str(self, instance):
        return instance.size_str

    def get_prices(self, instance):
        return {
            'plate_price': instance.plate_price,
            'mold_price': instance.mold_price,
            'shipping_price': instance.shipping_price,
            'unit_price': instance.unit_price,
            'product_total': instance.product_total,
            'subtotal': instance.subtotal,
            'tax': instance.tax,
            'total': instance.total,
        }

    def get_extra_info_str(self, instance):
        return instance.render_extra_info()

    def get_product_name(self, instance):
        return instance.product.name

    def get_product_image(self, instance):
        return instance.product.get_thumbnail_url()

    def get_product_url(self, instance):
        return instance.product.get_absolute_url()


class CartSerializer(serializers.ModelSerializer):

    num_items = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()
    prices = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        exclude = ['id', 'user', 'cart_id', 'last_changed', 'created_at', 'is_ordered']

    def get_num_items(self, instance):
        return instance.num_items

    def get_items(self, instance):
        items = []
        for i in instance.get_cart_items():
            items.append(CartItemSerializer(i).data)
        return items

    def get_prices(self, instance):
        return {
            'plate_price': instance.get_plate_total(),
            'mold_price': instance.get_mold_total(),
            'shipping_price': instance.get_shipping_total(),
            'product_total': instance.get_product_total(),
            'subtotal': instance.get_subtotal(),
            'tax': instance.get_tax(),
            'total': instance.get_total(),
        }
