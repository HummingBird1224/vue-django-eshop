from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django_mysql import models as mysql_model
from products.models import Product


User = get_user_model()


def get_mydesign_image_path(instance, filename):
    prefix = 'accounts/' + str(instance.user.id) + '/mydesign/'
    return prefix + filename


def get_mydesign_design_path(instance, filename):
    prefix = 'accounts/' + str(instance.mydesign.user.id) + '/mydesign/'
    return prefix + filename


class MyDesign(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    product_name = models.CharField(
        max_length=120,
        blank=True,
        null=True,
    )

    name = models.CharField(
        max_length=360,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    size = mysql_model.JSONField(
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to=get_mydesign_image_path,
        null=True,
        blank=True,
    )

    read_only_options = mysql_model.JSONField(
        null=True,
        blank=True
    )

    ordered_num = models.PositiveIntegerField(
        default=0
    )


class MyDesignDesign(models.Model):

    mydesign = models.OneToOneField(
        MyDesign,
        related_name='design',
        on_delete=models.CASCADE
    )

    data = models.FileField(
        upload_to=get_mydesign_design_path,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['ai', 'pdf', ])],
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
