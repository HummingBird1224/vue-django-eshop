from math import ceil
from copy import copy
import csv
import importlib

from django.core.exceptions import ValidationError
from django.core.validators import validate_slug, FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django_mysql import models as mysql_model
import requests


# IMAGE PATHS
def get_product_usecase_image_path(instance, filename):
    prefix = 'products/extra/usecase/'
    return prefix + filename



def get_product_usecase_icon_image_path(instance, filename):
    prefix = 'products/extra/usecase/'
    return prefix + filename


def get_product_category_icon_image_path(instance, filename):
    prefix = 'products/extra/category/'
    return prefix + filename


def get_product_category_tags_icon_image_path(instance, filename):
    prefix = 'products/extra/categorytags/'
    return prefix + filename


def get_product_thumbnail_path(instance, filename):
    prefix = 'products/products/' + instance.product.slug + '/thumbnail/'
    return prefix + filename


def get_product_image_path(instance, filename):
    prefix = 'products/products/' + instance.product.slug + '/cover/'
    return prefix + filename

def get_product_example_image_path(instance, filename):
    prefix = 'products/products/' + instance.product.slug + '/example/'
    return prefix + filename

def get_option_image_path(instance, filename):
    dirs = [instance.product.slug, instance.slug]
    prefix = 'products/options/' + '/'.join(dirs) + '/'
    return prefix + filename


def get_option_item_image_path(instance, filename):
    dirs = [instance.option.product.slug, instance.option.slug]
    prefix = 'products/options/' + '/'.join(dirs) + '/items/'
    return prefix + filename


def get_product_price_file_path(instance, filename):
    prefix = 'products/products/' + instance.product.slug + '/price/'
    return prefix + filename


def get_easydraft_area_image_path(instance, filename):
    prefix = 'products/products/' + instance.easydraft.product.slug + '/easy_draft/' + instance.easydraft.slug + '/'
    return prefix + filename


# MODELS
class ProductQuerySet(models.QuerySet):

    def all(self):
        return self.filter(is_active=True)

    def in_category(self, category):
        pks = []
        if category.get_children():
            for cat in category.get_children():
                for _ in self.filter(category=cat):
                    pks.append(_.pk)
            return self.filter(pk__in=pks)
        else:
            return self.filter(category=category)


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def in_category(self, category):
        return self.get_queryset().in_category(category)


class Product(models.Model):
    """ 商品
    """

    name = models.CharField(
        max_length=120,
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        max_length=120,
        validators=[validate_slug],
        unique=True,
    )

    category = models.ForeignKey(
        'ProductCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    usecase = models.ManyToManyField(
        'ProductUsecase',
        blank=True,
    )

    tags = models.ManyToManyField(
        'ProductTag',
        blank=True,
    )

    # 説明文
    overview = models.TextField(
        max_length=1000,
        null=True,
        blank=True
    )

    # 商品の数え方
    unit = models.CharField(
        max_length=12,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_custom_product = models.BooleanField(
        default=False,
    )

    objects = ProductManager()

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return self.name + ": " + self.slug

    def get_thumbnail_url(self):
        thumb = self.images.filter(is_hover_image=False).first()
        if thumb:
            return thumb.image.url
        return ''

    def get_hover_image_url(self):
        hover = self.images.filter(is_hover_image=True).first()
        if hover:
            return hover.image.url
        return ''

    def get_image_url_list(self):
        urls = [_.image.url for _ in self.images.all()]
        return urls

    def get_example_image_url_list(self):
        example_image_urls = [_.image.url for _ in self.example_images.all()]
        return example_image_urls

    def get_example_url_list(self):
        example_urls = [_.example_url for _ in self.example_images.all()]
        return example_urls

    def get_absolute_url(self):
        if self.is_custom_product:
            return None
        if not self.is_active:
            return reverse('home')
        # external service products
        cat_base = ProductCategory.objects.filter(slug='base').first()
        cat_colorme = ProductCategory.objects.filter(slug='colorme').first()
        cat_fujilogi = ProductCategory.objects.filter(slug='fujilogi').first()
        cat_futureshop = ProductCategory.objects.filter(slug='futureshop').first()
        if self.category == cat_base:
            return reverse('base_landing')
        elif self.category == cat_colorme:
            return reverse('colorme_landing')
        elif self.category == cat_fujilogi:
            return reverse('fujilogi_landing')
        elif self.category == cat_futureshop:
            return reverse('futureshop_landing')
        # default products
        return reverse(
            'product_detail',
            kwargs={
                'c_slug': self.category.get_parent_or_self().slug,
                'slug': self.slug
            }
        )

    def clean(self):
        """商品のデータが正しいかバリデーションかける
        """
        super().clean()

    def validate_price_vals(self, options):
        """価格計算のバリデーション
        TODO: パラメータの範囲等
        """
        # お問い合わせ必要商品
        # if self.info.is_contact_required:
        #     raise ValidationError("This product needs to be estimated offline.")

    def get_prices(self, options, reordered=False, from_mydesign=False):
        """全ての価格計算
        単価/版代/木型代/小計/合計を税抜きで計算
        """
        self.validate_price_vals(options)

        # カスタム商品
        # if self.is_custom_product:
        #     return

        # 式による計算
        unit_price = self._get_unit_price(options, validate=False)
        plate_price = self._get_plate_price(options, validate=False)
        mold_price = self._get_mold_price(options, validate=False)
        shipping_price = self._get_shipping_price(options, validate=False)

        quantity = int(options['quantity'])
        product_total = ceil(round(unit_price * quantity, 2))

        if reordered or from_mydesign:
            plate_price = 0
            mold_price = 0

        total_without_tax = product_total + plate_price + mold_price + shipping_price
        return (
            unit_price,
            plate_price,
            mold_price,
            product_total,
            shipping_price,
            total_without_tax,
        )

    def _get_price_class_path(self) -> str:
        return '.prices.{}'.format(self.slug.replace('-', '_'))

    # TODO: pricesモデルの親classを作ってtype hints
    def _get_price_module(self):
        return importlib.import_module(self._get_price_class_path(), package='products')

    def _get_unit_price(self, options, validate=True) -> float:
        """単価計算
        validateがTrueの場合はバリデーションかける
        原価計算関数の返り値はDecimalで返ってくるのでfloat化
        """
        if validate:
            self.validate_price_vals(options)

        price_module = self._get_price_module()
        unit_price = price_module.get_unit_price(options, {})
        return float(unit_price)

    def _get_plate_price(self, options, validate=True) -> int:
        """版代
        """
        if validate:
            self.validate_price_vals(options)
        self.validate_price_vals(options)

        price_module = self._get_price_module()
        plate_price = price_module.get_plate_price(options)
        return ceil(plate_price)

    def _get_mold_price(self, options, validate=True) -> int:
        """木型代
        """
        if validate:
            self.validate_price_vals(options)
        self.validate_price_vals(options)

        price_module = self._get_price_module()
        mold_price = price_module.get_mold_price(options)
        return ceil(mold_price)

    def _get_shipping_price(self, options, validate=True) -> int:
        """配送費
        """
        if validate:
            self.validate_price_vals(options)
        self.validate_price_vals(options)

        price_module = self._get_price_module()
        shipping_price = price_module.get_shipping_price(options)
        return ceil(shipping_price)


class ProductInfo(models.Model):
    """ 商品の追加情報
    """

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='info',
    )

    # サイト上で注文可能か
    can_order_on_site = models.BooleanField(
        default=False,
    )

    # お問い合わせ商品か
    is_contact_required = models.BooleanField(
        default=False,
    )

    contact_url = models.URLField(
        null=True,
        blank=True,
    )

    # サンプル注文できるか
    can_order_sample = models.BooleanField(
        default=False,
    )

    # 最小注文数
    min_ordering_quantity = models.PositiveIntegerField(
        default=0
    )

    # 最大注文数
    max_ordering_quantity = models.PositiveIntegerField(
        default=0
    )

    # 初回注文時の目安納期（日数）
    estimated_shipping_date_first = models.PositiveIntegerField(
        default=0
    )

    # 再注文時の目安納期（日数）
    estimated_shipping_date_repeat = models.PositiveIntegerField(
        default=0
    )

    # オリジナルサイズ注文可能か
    can_select_original_size = models.BooleanField(
        default=False,
    )

    # デザインの入稿が必要か
    is_design_necessary = models.BooleanField(
        default=True,
    )

    # カンタン入稿可能か
    is_easy_draft_available = models.BooleanField(
        default=False,
    )

    # 備考(key:valueの形式)
    notes = mysql_model.JSONField(
        null=True,
        blank=True
    )

    # 配送可能都道府県
    shipping_area = mysql_model.JSONField(
        null=True,
        blank=True
    )

    # サイズ制限
    size_limit = mysql_model.JSONField(
        null=True,
        blank=True
    )

    # 選択可能色
    choosable_color = mysql_model.JSONField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.product.name + "詳細"


class ProductPrice(models.Model):
    """商品価格リスト
    """

    product = models.OneToOneField(
        Product,
        related_name='price',
        on_delete=models.CASCADE,
    )

    refer_to = models.CharField(
        max_length=120,
        choices=(
            ('url', 'url'),
            ('csv', 'csv'),
        ),
        default='url'
    )

    url = models.URLField(
        null=True,
        blank=True,
    )

    key = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )

    csv = models.FileField(
        upload_to=get_product_price_file_path,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['csv', ])],
    )

    sample_unit_price = models.FloatField(
        null=True,
        blank=True,
    )

    sample_lot = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.product.name + "価格"

    def validate_price_vals(self, options):
        """価格計算のバリデーション
        TODO: パラメータの範囲等
        """
        # お問い合わせ必要商品
        # if self.product.info.is_contact_required:
        #     raise ValidationError("This product needs to be estimated offline.")

    def get_prices(self, data, listed=False):
        data['listed'] = listed
        if self.refer_to == 'url':
            res = requests.post(self.url, json=data)
            return res.json()
        elif self.refer_to == 'csv':
            self._get_price_from_csv(self, data)

    def _get_price_from_csv(self, options):
        """ CSVから値段を取ってくる
        """
        key_list = []
        keys = self.key.split(' ')
        for _k in keys:
            if _k in ['height', 'width', 'depth']:
                key_list.append(str(options['size'][_k]))
            else:
                key_list.append(str(options[_k]))
        key = " ".join(key_list)
        with self.csv.open('r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['key'] == key:
                    return (float(row['unit price']),
                            int(row['plate price']),
                            int(row['mold price']),
                            int(row['shipping price']),)
        raise KeyError("Key is not valid.")


class ProductOption(models.Model):
    """ 商品に関する選択項目
    選択肢はProductOptionItem
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='options',
    )

    slug = models.SlugField()

    name = models.CharField(
        max_length=360,
    )

    detail = models.TextField(
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to=get_option_image_path,
        null=True,
        blank=True,
    )

    required = models.BooleanField(
        default=True
    )

    position = models.PositiveSmallIntegerField(
        default=1,
    )

    widget_type = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    modal_blocks = mysql_model.JSONField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['product', 'position']

    def __str__(self):
        return self.product.slug + " " + self.slug


class ProductOptionItem(models.Model):
    """ 商品に関する選択項目
    選択肢はProductOptionItem
    """

    option = models.ForeignKey(
        ProductOption,
        on_delete=models.CASCADE,
        related_name='items',
    )

    name = models.CharField(
        max_length=360,
        null=True,
        blank=True,
    )

    # valueがサイズのように複数の場合delimiterで区切る
    delimiter = models.CharField(
        max_length=8,
        null=True,
        blank=True,
    )

    value = models.CharField(
        max_length=360,
        null=True,
        blank=True,
    )

    detail = models.TextField(
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to=get_option_item_image_path,
        null=True,
        blank=True,
    )

    is_default = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    is_reorderable = models.BooleanField(
        default=True
    )

    position = models.PositiveSmallIntegerField(
        default=1,
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.option.__str__() + " " + self.name


class ProductOptionCondition(models.Model):

    item = models.ForeignKey(
        ProductOptionItem,
        on_delete=models.CASCADE,
        related_name='condition',
    )

    operator = models.CharField(
        max_length=120
    )

    option = models.ForeignKey(
        ProductOption,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    values = models.ManyToManyField(
        ProductOptionItem,
    )

    def __str__(self):
        return self.item.__str__()

    def clean(self):
        super().clean()
        for val in self.values.all():
            if val.option != self.option:
                raise ValidationError('option and items are mismatched.')


class ProductCategoryQuerySet(models.QuerySet):

    def public(self):
        external = self.filter(slug='external')
        return self.filter(is_active=True).exclude(slug='external').exclude(parent_category__in=external)


class ProductCategoryManager(models.Manager):

    def get_queryset(self):
        return ProductCategoryQuerySet(self.model, using=self._db)

    def public(self):
        return self.get_queryset().public()


class ProductCategory(models.Model):
    """ 商品カテゴリ
    """

    parent_category = models.ForeignKey(
        'ProductCategory',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=120,
    )

    slug = models.SlugField(
        max_length=120,
        validators=[validate_slug],
        unique=True,
    )

    detail = models.TextField(
        max_length=400,
        null=True,
        blank=True,
    )

    icon = models.FileField(
        upload_to=get_product_category_icon_image_path,
        null=True,
        blank=True,
    )

    tags = models.ManyToManyField(
        'ProductCategoryTag',
        blank=True,
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True
    )

    position = models.PositiveSmallIntegerField(
        default=10000,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    objects = ProductCategoryManager()

    class Meta:
        ordering = ['position']

    def __str__(self):
        ret = self.name
        parent = self.parent_category
        while parent:
            ret = parent.name + " > " + ret
            parent = parent.parent_category
        return ret

    @property
    def has_children(self):
        if self.get_children():
            return True
        return False

    def get_parent_or_self(self):
        cat = self
        root = ProductCategory.objects.filter(slug='root').first()
        while cat.parent_category and cat.parent_category != root:
            cat = cat.parent_category
        return cat

    def get_children(self):
        return [cat for cat in ProductCategory.objects.filter(is_active=True, parent_category=self)]


class ProductCategoryTag(models.Model):

    name = models.CharField(
        max_length=128
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True
    )

    url = models.URLField(
        max_length=200,
        null=True,
        blank=True,
    )

    position = models.PositiveSmallIntegerField(
        default=10000,
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name


class ProductTag(models.Model):

    name = models.CharField(
        max_length=128
    )

    color = models.CharField(
        max_length=16,
        null=True,
        blank=True
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class ProductUsecase(models.Model):

    name = models.CharField(
        max_length=128,
    )

    slug = models.SlugField(
        max_length=120,
        validators=[validate_slug],
        unique=True,
    )

    content = models.TextField(
        max_length=300,
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to=get_product_usecase_image_path,
        null=True,
        blank=True,
    )

    icon = models.ImageField(
        upload_to=get_product_usecase_icon_image_path,
        null=True,
        blank=True,
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
    )

    image = models.ImageField(
        upload_to=get_product_image_path
    )

    alt_text = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_hover_image = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    position = models.PositiveSmallIntegerField(
        default=1
    )

    class Meta:
        ordering = ('position', )


class ProductExampleImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='example_images',
    )

    image = models.ImageField(
        upload_to=get_product_example_image_path
    )

    example_url = models.URLField(
        max_length=300,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_active = models.BooleanField(
        default=True
    )

    position = models.PositiveSmallIntegerField(
        default=1
    )

    class Meta:
        ordering = ('position', )


class EasyDraft(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='easydrafts',
    )

    slug = models.SlugField(
        max_length=120,
        validators=[validate_slug],
    )

    pdf_height = models.PositiveIntegerField(
        default=0
    )

    pdf_width = models.PositiveIntegerField(
        default=0
    )

    image_height = models.PositiveIntegerField(
        default=0
    )

    image_width = models.PositiveIntegerField(
        default=0
    )

    pdf_background_color = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )

    pdf_border_color = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.product.name + ": " +  self.product.slug


class EasyDraftPrintArea(models.Model):

    easydraft = models.ForeignKey(
        EasyDraft,
        on_delete=models.CASCADE,
        related_name='printareas',
    )

    name = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )

    area_id = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to=get_easydraft_area_image_path
    )

    is_printable = models.BooleanField(
        default=True
    )

    image_pos_start_x = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )

    image_pos_start_y = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )

    image_pos_end_x = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )

    image_pos_end_y = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )

    pdf_pos_start_x = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )

    pdf_pos_start_y = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )

    pdf_pos_end_x = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )

    pdf_pos_end_y = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )


# Product作成時にProductInfoとProductPriceも同時作成
def post_save_product(sender, instance, created, **kwargs):
    if created:
        ProductInfo.objects.create(product=instance)
        ProductPrice.objects.create(product=instance)


post_save.connect(post_save_product, sender=Product)
