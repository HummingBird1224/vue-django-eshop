from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from products.models import Product
from django_mysql import models as mysql_model
from math import ceil


User = get_user_model()


class CartManager(models.Manager):

    def _get_cart_id(self, request):
        cart_id = request.session.get('cart', None)
        return cart_id

    def get_from_request(self, request):
        cart_id = self._get_cart_id(request)
        cart = Cart.objects.filter(id=cart_id).first()
        if not cart and request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
            request.session['cart'] = cart.id
        return cart

    def get_or_create_from_request(self, request):
        cart = self.get_from_request(request)
        if not cart:
            cart = Cart.objects.create()
            request.session['cart'] = cart.id
        return cart

    def clear_cart(self, request):
        return request.session.pop('cart', None)


class Cart(models.Model):

    cart_id = models.CharField(
        max_length=250,
        blank=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    last_changed = models.DateTimeField(
        auto_now=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_ordered = models.BooleanField(
        default=False
    )

    objects = CartManager()

    def __str__(self):
        return "{}".format(self.pk) if self.pk else "(unsaved)"

    @property
    def num_items(self):
        return self.items.in_cart().count()

    @property
    def is_empty(self):
        return self.num_items == 0

    def empty(self):
        """カートを空にする
        """
        if self.pk:
            self.items.all().delete()
            self.delete()

    def get_cart_items(self):
        return self.items.in_cart()

    def get_product_total(self):
        """商品の価格合計
        """
        total = 0
        for item in self.get_cart_items():
            total += item.product_total
        return total

    def get_plate_total(self):
        """版代合計
        """
        total = 0
        for item in self.get_cart_items():
            total += item.plate_price
        return total

    def get_mold_total(self):
        """木型代合計
        """
        total = 0
        for item in self.get_cart_items():
            total += item.mold_price
        return total

    def get_shipping_total(self):
        """配送料
        """
        total = 0
        for item in self.get_cart_items():
            total += item.shipping_price
        return total

    def get_subtotal(self):
        """商品価格/版代/木型代/配送料の合計
        """
        return self.get_product_total() + self.get_plate_total() + self.get_mold_total() + self.get_shipping_total()

    def get_tax(self):
        """消費税
        """
        total = 0
        for item in self.get_cart_items():
            total += item.tax
        return total

    def get_total(self):
        """合計
        """
        return self.get_subtotal() + self.get_tax()

    def update(self):
        """カートの内容（価格）を更新する
        """
        for item in self.get_cart_items():
            item.update()

    def merge_with(self, other_cart):
        """２つのカートをがっちゃんこする
        """
        if self.id == other_cart.id:
            raise RuntimeError("Can not merge cart with itself")
        other_cart.items.update(cart=self)
        other_cart.delete()


class CartItemQuerySet(models.QuerySet):

    def in_cart(self):
        return self.filter(in_cart=True)


class CartItemManager(models.Manager):

    def get_queryset(self):
        return CartItemQuerySet(self.model, using=self._db)

    def in_cart(self):
        return self.get_queryset().in_cart()


class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        related_name='items',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField()

    prices = mysql_model.JSONField(
        null=True,
        blank=True,
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    in_cart = models.BooleanField(
        default=True
    )

    objects = CartItemManager()

    def __str__(self):
        if self.product:
            return self.product.name
        return "Deleted Product"

    @property
    def is_valid(self):
        return True

    @property
    def size_str(self):
        h = self.extra_info.get('height')
        w = self.extra_info.get('width')
        d = self.extra_info.get('depth')

        # new structure
        size = self.extra_info.get('size')
        if size and not h:
            h = size.get('height')
        if size and not w:
            w = size.get('width')
        if size and not d:
            d = size.get('depth')

        h_str = "高さ: " + str(h) + "mm" if h else None
        w_str = "幅: " + str(w) + "mm" if w else None
        d_str = "奥行き: " + str(d) + "mm" if d else None
        return " + ".join([_ for _ in [w_str, d_str, h_str] if _])

    @property
    def color_num(self):
        return self.extra_info['color_num']

    @property
    def plate_price(self):
        return self.prices.get('plate_price', 0)

    @property
    def mold_price(self):
        return self.prices.get('mold_price', 0)

    @property
    def shipping_price(self):
        return self.prices.get('shipping_price', 0)

    @property
    def unit_price(self):
        return self.prices.get('unit_price', 0)

    @property
    def product_total(self):
        return self.prices.get('product_total', 0)

    @property
    def subtotal(self):
        return self.prices.get('subtotal', 0)

    @property
    def tax(self):
        return self.prices.get('tax', 0)

    @property
    def total(self):
        return self.prices.get('total', 0)

    def update(self):
        """価格更新
        もし再注文だったら（extra_infoにフラグ）単価以外は更新しない。
        """
        (unit_price, plate_price, mold_price, product_total, shipping_price, total_without_tax) = \
            self.product.get_prices(self.extra_info,
                                    reordered=self.extra_info.get('reordered', False),
                                    from_mydesign=self.extra_info.get('from_mydesign', False))
        tax = ceil(total_without_tax * settings.TAX_RATE)
        self.prices['unit_price'] = unit_price
        self.prices['plate_price'] = plate_price
        self.prices['mold_price'] = mold_price
        self.prices['product_total'] = product_total
        self.prices['shipping_price'] = shipping_price
        self.prices['subtotal'] = total_without_tax
        self.prices['tax'] = tax
        self.prices['total'] = total_without_tax + tax
        self.save()

    def render_extra_info(self):
        # TODO: 商品自体が削除されていると使えないからカートのextra_infoに全部いれておいたほうがいいかも
        #       これはOrder modelも同じ
        rendered_info = {}
        for key, val in self.extra_info.items():
            if key != 'size':
                option = self.product.options.filter(slug=key).first()
                if option:
                    item = option.items.filter(value=val).first()
                    if item:
                        rendered_info[option.name] = item.name
        return rendered_info
