from rest_framework import serializers
from .models import MyDesign
from products.serializers import ProductOptionSerializer


class MyDesignSerializer(serializers.ModelSerializer):

    size = serializers.SerializerMethodField(read_only=True)
    length_sum = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MyDesign
        fields = ['product_name',
                  'name',
                  'size',
                  'length_sum',
                  'image',
                  'id']

    def get_size(self, obj):
        h = obj.size.get('height')
        w = obj.size.get('width')
        d = obj.size.get('depth')

        h_str = str(h) + "mm" if h else None
        w_str = str(w) + "mm" if w else None
        d_str = str(d) + "mm" if d else None
        return "×".join([_ for _ in [h_str, w_str, d_str] if _])

    def get_length_sum(self, obj):
        h = obj.size.get('height')
        w = obj.size.get('width')
        d = obj.size.get('depth')
        if h and w and d:
            return sum([h, w, d])
        return None

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return obj.product.get_thumbnail_url()


class MyDesignReorderSerializer(serializers.ModelSerializer):

    slug = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)
    unit = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    shipping_date = serializers.SerializerMethodField(read_only=True)
    read_only_options_str = serializers.SerializerMethodField(read_only=True)
    options = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MyDesign
        fields = ['product_name',
                  'name',
                  'slug',
                  'category',
                  'unit',
                  'image',
                  'shipping_date',
                  'read_only_options',
                  'read_only_options_str',
                  'options']

    def get_slug(self, obj):
        return obj.product.slug

    def get_category(self, obj):
        return obj.product.category.get_parent_or_self().name

    def get_unit(self, obj):
        return obj.product.unit

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return obj.product.get_thumbnail_url()

    def get_shipping_date(self, obj):
        return obj.product.info.estimated_shipping_date_repeat

    def get_read_only_options_str(self, obj):
        rendered_info = {}
        for key, val in obj.read_only_options.items():
            if key != 'size':
                option = obj.product.options.filter(slug=key).first()
                if option:
                    item = option.items.filter(value=val).first()
                    if item:
                        rendered_info[option.name] = item.name
        return rendered_info

    def get_options(self, obj):
        # 今は注文数だけ変更可能
        option = obj.product.options.filter(slug='quantity').first()
        return ProductOptionSerializer(option).data
