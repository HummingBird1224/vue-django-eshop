from django.db import models
from products.models import Product
import re

def get_casestudy_image_path(instance, filename):
    # dirs = [instance.option.product.slug, instance.option.slug]
    dirs = ""
    prefix = 'casestudies/casestudy/' + '/'.join(dirs)
    return prefix + filename

def get_casestudy_category_icon_path(instance, filename):
    # dirs = [instance.option.product.slug, instance.option.slug]
    dirs = ""
    prefix = 'casestudies/casestudy_category/icons/' + '/'.join(dirs) + '/items/'
    return prefix + filename

def get_casestudy_category_image_path(instance, filename):
    # dirs = [instance.option.product.slug, instance.option.slug]
    dirs = ""
    prefix = 'casestudies/casestudy_category/images/' + '/'.join(dirs) + '/items/'
    
    # prefix = 'casestudies/casestudy_category/images/' + '/items/'
    return prefix + filename
    
def get_casestudy_category_explanatory_image_path(instance, filename):
    # dirs = [instance.option.product.slug, instance.option.slug]
    dirs = ""
    prefix = 'casestudies/casestudy_category/explanations/' + '/'.join(dirs) + '/items/'
    return prefix + filename

# Create your models here.
class CaseStudyCategoryQuerySet(models.QuerySet):

    def public(self):
        external = self.filter(slug='external')
        return self.filter(is_active=True).exclude(slug='external').exclude(category__in=external)
    
    def get_category_children(self):
        # return  CaseStudyCategory.objects.filter(is_active=True, category=self)
        return self.filter(is_active=True, category=self)
        

class CaseStudyQuerySet(models.QuerySet):

    def public(self):
        
        return self.filter(is_active=True)


class CaseStudyCategoryManager(models.Manager):

    def get_queryset(self):
        return CaseStudyCategoryQuerySet(self.model, using=self._db)

    def public(self):
        return self.get_queryset().public()



class CaseStudyManager(models.Manager):

    def get_queryset(self):
        return CaseStudyQuerySet(self.model, using=self._db)

    def public(self):
        return self.get_queryset().public()

    # def public(self):
    #     return self.filter(is_active=True)
    

class CaseStudyCategory(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="名称",
    )

    slug = models.SlugField(
        max_length=120,
        unique=True,
    )

    category = models.ForeignKey(
        'CaseStudyCategory',
        blank=True,
        null=True,
        verbose_name="カテゴリ",
        on_delete=models.CASCADE
    )
    
    overview = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="概要"
    )

    text = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="説明文"
    )

    advantage =  models.TextField(
        null=True,
        blank=True,
        verbose_name="メリット"
    )

    disadvantage =  models.TextField(
        null=True,
        blank=True,
        verbose_name="デメリット"
    )

    explanatory_image = models.ImageField(
        upload_to=get_casestudy_category_explanatory_image_path,
        null=True,
        blank=True,
        verbose_name="説明画像"
    )

    icon = models.ImageField(
        upload_to=get_casestudy_category_icon_path,
        null=True,
        blank=True,
        verbose_name="アイコン"
    )

    image = models.ImageField(
        upload_to=get_casestudy_category_image_path,
        null=True,
        blank=True,
        verbose_name="画像"
    )

    URL = models.URLField(
        null=True,
        blank=True,        
        verbose_name="URL"
    )

    position = models.PositiveSmallIntegerField(
        default=1,
    )
    
    is_active = models.BooleanField(
        default=True,
    )

    objects = CaseStudyCategoryManager()

    class Meta:
        ordering = ['position']

    def __str__(self):
        ret = self.name
        parent = self.category
        while parent:
            if parent.name != 'root':
                ret = parent.name + " > " + ret
            parent = parent.category
        return ret
# plz study about these parts.

    @property
    def has_children(self):
        if self.get_children():
            return True
        return False

    def get_parent_or_self(self):
        cat = self
        root = CaseStudyCategory.objects.filter(slug='root').first()
        while cat.category and cat.category != root:
            cat = cat.category
        return cat

    def get_children(self):
        # return  CaseStudyCategory.objects.filter(is_active=True, category=self)
        return [cat for cat in CaseStudyCategory.objects.filter(is_active=True, category=self)]


class CaseStudy(models.Model): 
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="商品"
    )

    title = models.CharField(
        max_length=255,
        verbose_name="タイトル",
    )

    client = models.CharField(
        max_length=255,
        verbose_name="顧客名",
    )
    
    slug = models.SlugField(
        max_length=120,
        unique=True,
    )

    text = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="説明文",
    )

    text_url = models.URLField(
        null=True,
        blank=True,    
        verbose_name="説明文 URL"
    )

    product_category = models.ManyToManyField(
        CaseStudyCategory,
        related_name='product_category',
        blank=True,
        verbose_name="商品区分"
    )

    shape = models.ManyToManyField(
        CaseStudyCategory,
        related_name="shape",
        blank=True,
        verbose_name="形状"
    )

    printing_method = models.ManyToManyField(
        CaseStudyCategory,
        related_name="printing_method",
        blank=True,
        verbose_name="印刷方法"
    )

    material = models.ManyToManyField(
        CaseStudyCategory,
        related_name="material",
        blank=True,
        verbose_name="材質",
    )

    usage = models.ManyToManyField(
        CaseStudyCategory,
        related_name="usage",
        blank=True,
        verbose_name="用途"
    )

    processing = models.ManyToManyField(
        CaseStudyCategory,
        related_name="processing",
        blank=True,
        verbose_name="加工"
    )

    sustainability = models.ManyToManyField(
        CaseStudyCategory,
        related_name="sustainability",
        blank=True,
        verbose_name="環境配慮"
    )

    position = models.PositiveSmallIntegerField(
        default=1,
    )

    is_active = models.BooleanField(
        default=True,
    )
    objects = CaseStudyManager()
    
    class Meta:
        ordering = ['position']

    def get_image_url_list(self):
        urls = [_.image.url for _ in self.images.all()]
        # print(urls)
        return urls

    def get_hover_image_url(self):
        hover = self.images.filter(is_hover_image=True).first()
        if hover:
            return hover.image.url
        return ''

class CaseStudyImage(models.Model):

    casestudy = models.ForeignKey(
        CaseStudy,
        on_delete=models.CASCADE,
        related_name='images',
    )

    image = models.ImageField(
        upload_to=get_casestudy_image_path,
        verbose_name="画像"
    )
    
    is_hover_image = models.BooleanField(
        default=False
    )

    position = models.PositiveSmallIntegerField(
        default=1
    )

    class Meta:
        ordering = ('position', )
