from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.http import urlencode
from django.utils.translation import ugettext_lazy as _, pgettext_lazy, get_language_from_request
from django.urls import reverse
from django_mysql import models as mysql_model
from ipware import get_client_ip
from products.models import Product
from accounts.models import DeliveryAddress, BillingAddress
from canal.choices import PREFECTURES
from utils.payment_functions import (
    cancel_transaction,
    capture_from_order,
    remake_transaction,
)


User = get_user_model()


class OrderManager(models.Manager):

    def get_current_order(self, request):
        ref = request.session.get('order', None)
        try:
            order = self.get_queryset().get(ref_code=ref)
        except self.model.DoesNotExist as e:
            raise e
        if request.user.is_authenticated:
            if order.user != request.user:
                raise self.model.DoesNotExist()
        return order

    def set_current_order(self, request, oid):
        request.session['order'] = oid
        if request.user.is_authenticated:
            order = self.get_queryset().get(ref_code=oid)
            order.user = request.user
            order.save()

    def clear_order(self, request):
        return request.session.pop('order', None)

    def create_from_cart(self, cart, request):
        pass

    def stored_request(self, request):
        """購入時のrequestの内容
        ip, 言語, user agent等
        """
        return {
            'language': get_language_from_request(request),
            'absolute_base_uri': request.build_absolute_uri('/'),
            'remote_ip': get_client_ip(request),
            'user_agent': request.META.get('HTTP_USER_AGENT'),
        }


class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
    )

    state = models.CharField(
        max_length=32,
        choices=(('new', 'new'),
                 ('created', 'created'),
                 ('charge_confirmed', 'charge_confirmed'),
                 ('charge_declined', 'charge_declined')),
        default='new'
    )

    ref_code = models.CharField(
        max_length=120,
        unique=True
    )

    # PRICES
    product_total = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    plate_total = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    mold_total = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    shipping_total = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    tax_total = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    currency = models.CharField(
        max_length=7,
        editable=False,
        default='JPY',
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_charged = models.BooleanField(
        default=False
    )

    showed_confirmation = models.BooleanField(
        default=False
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True,
    )

    stored_request = mysql_model.JSONField(
        help_text=_("Parts of the Request objects on the moment of purchase."),
    )

    objects = OrderManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.ref_code)

    def get_order_items(self):
        return self.items.all().exclude(payment='cancelled')

    def get_subtotal(self):
        return sum([item.subtotal for item in self.get_order_items()])

    def get_billing_url(self):
        return "".join([reverse('billing'), '?', urlencode(dict(oid=self.ref_code))])

    def get_transaction(self):
        from billing.models import Transaction
        return Transaction.objects.filter(order=self).first()

    def update_prices(self):
        product_total = 0
        plate_total = 0
        mold_total = 0
        shipping_total = 0
        tax_total = 0
        for item in self.get_order_items():
            product_total += item.prices.get('product_total', 0)
            plate_total += item.prices.get('plate_price', 0)
            mold_total += item.prices.get('mold_price', 0)
            shipping_total += item.prices.get('shipping_price', 0)
            tax_total += item.prices.get('tax', 0)
        total = product_total + plate_total + mold_total + shipping_total + tax_total
        self.product_total = product_total
        self.plate_total = plate_total
        self.mold_total = mold_total
        self.shipping_total = shipping_total
        self.tax_total = tax_total
        self.total = total
        self.save()


class OrderDeliveryAddress(models.Model):

    order = models.OneToOneField(
        Order,
        related_name='delivery_address',
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    # OBSOLETE
    first_name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    # OBSOLETE
    last_name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    postal_code = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )

    prefecture = models.CharField(
        max_length=12,
        choices=PREFECTURES,
        null=True,
        blank=True
    )

    city = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    building = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    tel = models.CharField(
        max_length=36,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.get_full_name() + ": " + self.get_full_address()

    def get_full_address(self):
        return "".join([str(_) for _ in [self.prefecture, self.city, self.building] if _])

    def get_address_with_prefecture(self):
        return "".join([str(_) for _ in [self.city, self.building] if _])

    def get_full_name(self):
        # Add prefix and return full name
        return "".join([str(_) for _ in [self.name, ] if _])


class OrderBillingAddress(models.Model):

    order = models.OneToOneField(
        Order,
        related_name='billing_address',
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    # OBSOLETE
    first_name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    # OBSOLETE
    last_name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    postal_code = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )

    prefecture = models.CharField(
        max_length=12,
        choices=PREFECTURES,
        null=True,
        blank=True
    )

    city = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    building = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    tel = models.CharField(
        max_length=36,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.get_full_name() + ": " + self.get_full_address()

    def get_full_address(self):
        return "".join([str(_) for _ in [self.prefecture, self.city, self.building] if _])

    def get_address_with_prefecture(self):
        return "".join([str(_) for _ in [self.city, self.building] if _])

    def get_full_name(self):
        # Add prefix and return full name
        return "".join([str(_) for _ in [self.name, ] if _])


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )

    ref_code = models.CharField(
        max_length=120,
        unique=True
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    product_name = models.CharField(
        max_length=350
    )

    product_slug = models.CharField(
        max_length=350,
        null=True,
        blank=True,
    )

    quantity = models.PositiveIntegerField(
        editable=False,
    )

    prices = mysql_model.JSONField(
        null=True,
        blank=True,
        editable=False,
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    payment = models.CharField(
        max_length=32,
        choices=(('pending', 'pending'),
                 ('confirmed', 'confirmed'),
                 ('paid', 'paid'),
                 ('cancelled', 'cancelled')),
        default='pending'
    )

    draftprompt_edited_at = models.DateTimeField(
        null=True,
        blank=True
    )

    payprompt_edited_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.product_name

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

    @property
    def state(self):
        if self.payment == 'cancelled':
            return 'cancelled'
        if self.design.state != 'confirmed':
            return self.design.state
        return self.delivery.state

    @property
    def internal_state(self):
        if self.payment == 'cancelled':
            return 'cancelled'
        if self.is_in_design_phase:
            return self.design.state
        return self.delivery.state

    @property
    def internal_state_display(self):
        if self.payment == 'cancelled':
            return 'キャンセル済'
        if self.is_in_design_phase:
            return self.design.get_state_display()
        return self.delivery.get_state_display()

    @property
    def is_in_design_phase(self):
        return self.delivery.state == 'unassigned'

    @transaction.atomic
    def cancel_atomic(self):
        # CHANGE STATUS (CANCEL) OF THE SELECTED ITEM
        self.payment = 'cancelled'
        self.save()

        # CREDIT CARD REFUND
        cancel_transaction(self.order)
        self.order.update_prices()
        # IF THERE ARE STILL ITEMS IN THE ORDER
        if self.order.get_order_items():
            remake_transaction(self.order)
            capture_from_order(self.order)
        # IF NO ITEM IN THE ORDER
        else:
            self.order.state = 'charge_declined'
            self.order.save()

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

    def is_reorderable(self):
        _ = []
        for key, val in self.extra_info.items():
            option = self.product.options.filter(slug=key).first()
            if option:
                item = option.items.filter(value=val).first()
                if option.slug == 'size':
                    size_dict = self.extra_info.get('size')
                    _val = ", ".join([str(size_dict[key]) for key in ['height', 'width', 'depth'] if key in size_dict])
                    item = option.items.filter(value=_val).first()
                # TODO: print_area
                if item:
                    _.append(item.is_reorderable)
        return all(_)


def get_order_design_file_path(instance, filename):
    prefix = 'orders/design/'
    user_id = instance.item.order.user.id
    return prefix + str(user_id) + "/" + filename


def get_provisional_order_design_file_path(instance, filename):
    prefix = 'orders/design/'
    user_id = instance.item.order.user.id
    return prefix + str(user_id) + "/" + filename


class OrderItemDesign(models.Model):

    item = models.OneToOneField(
        OrderItem,
        related_name='design',
        on_delete=models.CASCADE
    )

    data = models.FileField(
        upload_to=get_order_design_file_path,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['ai', 'pdf', ])],
    )

    comment = models.TextField(
        max_length=500,
        null=True,
        blank=True,
    )

    state = models.CharField(
        max_length=64,
        choices=(('not_submitted', '未入稿'),
                 ('under_check', '確認中'),
                 ('resubmission_request', '再入稿依頼'),
                 ('checked', '確認済'),
                 ('confirmed', '承認済')),
        default="not_submitted"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.state

    def human_readable_filesize(self, suffix='B'):
        _datasize = self.data.size
        for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
            if abs(_datasize) < 1024.0:
                return "%3.1f%s%s" % (_datasize, unit, suffix)
            _datasize /= 1024.0
        return "%.1f%s%s" % (self.data.size, 'Y', suffix)

    def save(self, **kwargs):
        queryset = OrderItemDesign.objects
        if queryset.filter(id=self.id).exists() and self.item.is_in_design_phase:
            prev_obj = queryset.get(id=self.id)
            prev_state = prev_obj.state if prev_obj.item.is_in_design_phase else prev_obj.item.delivery.state
            state = self.state
            if prev_state != state:
                LogOrderItemStateUpdate.objects.create(item=self.item, prev_val=prev_state, val=state)
        super(OrderItemDesign, self).save(**kwargs)


class ProvisionalOrderItemDesign(models.Model):

    item = models.OneToOneField(
        OrderItem,
        related_name='provisional_design',
        on_delete=models.CASCADE
    )

    data = models.FileField(
        upload_to=get_order_design_file_path,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['ai', 'pdf', ])],
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def human_readable_filesize(self, suffix='B'):
        _datasize = self.data.size
        for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
            if abs(_datasize) < 1024.0:
                return "%3.1f%s%s" % (_datasize, unit, suffix)
            _datasize /= 1024.0
        return "%.1f%s%s" % (self.data.size, 'Y', suffix)


class OrderItemDelivery(models.Model):

    item = models.OneToOneField(
        OrderItem,
        related_name='delivery',
        on_delete=models.CASCADE,
    )

    state = models.CharField(
        max_length=64,
        choices=(('unassigned', '未手配'),
                 ('printing', '印刷中'),
                 ('shipped', '発送済'),
                 ('delivered', '宅配済')),
        default='unassigned',
    )

    company = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    tracking_code = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    shipping_date = models.DateField(
        null=True,
        blank=True
    )

    delivery_date = models.DateField(
        null=True,
        blank=True
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True
    )

    address = models.ForeignKey(
        DeliveryAddress,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    # OBSOLETE
    first_name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    # OBSOLETE
    last_name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    postal_code = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )

    prefecture = models.CharField(
        max_length=12,
        choices=PREFECTURES,
        null=True,
        blank=True
    )

    city = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    building = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    tel = models.CharField(
        max_length=36,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.get_full_name() + ": " + self.get_full_address()

    def get_full_address(self):
        return "".join([str(_) for _ in [self.prefecture, self.city, self.building] if _])

    def get_address_with_prefecture(self):
        return "".join([str(_) for _ in [self.city, self.building] if _])

    def get_full_name(self):
        return "".join([str(_) for _ in [self.name, ] if _])

    @property
    def shipping_date_display(self):
        return self.shipping_date if self.shipping_date is not None else "---"

    @property
    def delivery_date_display(self):
        return self.delivery_date if self.delivery_date is not None else "---"

    def save(self, **kwargs):
        queryset = OrderItemDelivery.objects
        if queryset.filter(id=self.id).exists() and not self.item.is_in_design_phase:
            prev_obj = queryset.get(id=self.id)
            prev_state = prev_obj.state if not prev_obj.item.is_in_design_phase else prev_obj.item.design.state
            state = self.state
            if prev_state != state:
                LogOrderItemStateUpdate.objects.create(item=self.item, prev_val=prev_state, val=state)

        super(OrderItemDelivery, self).save(**kwargs)


class LogOrderItemStateUpdate(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    item = models.ForeignKey(
        OrderItem,
        on_delete=models.PROTECT,
        null=True
    )

    prev_val = models.CharField(
        max_length=514
    )

    val = models.CharField(
        max_length=514
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


@receiver(post_save, sender=OrderItem)
def post_save_order_item(sender, instance, created, **kwargs):
    if created:
        OrderItemDesign.objects.create(item=instance)
        ProvisionalOrderItemDesign.objects.create(item=instance)
        OrderItemDelivery.objects.create(item=instance)
