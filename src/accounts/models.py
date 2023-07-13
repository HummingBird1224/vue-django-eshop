from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django_mysql import models as mysql_model
from utils.payjp_functions import payjp_create_customer
from canal.choices import PREFECTURES
import logging
from .validators import validate_tel, validate_postal_code


logger = logging.getLogger(__name__)


class UserQuerySet(models.QuerySet):

    def staffs(self):
        return self.filter(is_staff=True)

    def all(self):
        return self.filter(is_active=True)


class UserManager(BaseUserManager):

    def _create_user(self, email, company_name, name, password=None, **extra_fields):
        user = self.model(
            email=email,
            company_name=company_name,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, company_name, name, password=None, **extra_fields):
        user = self._create_user(email, company_name, name, password, **extra_fields)
        user.save(using=self._db)
        logger.info("Created user with email:{}, name:{}.".format(email, name))
        return user

    def create_superuser(self, email, company_name, name, password=None, **extra_fields):
        user = self._create_user(email, company_name, name, password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        logger.info("Created a super user.")
        return user

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)


class User(AbstractBaseUser):

    email = models.EmailField(
        unique=True,
        verbose_name="メールアドレス",
    )

    company_name = models.CharField(
        max_length=255,
        verbose_name="会社名",
        blank=True,
        null=True
    )

    name = models.CharField(
        max_length=255,
        verbose_name="名前",
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    url = models.URLField(
        max_length=200,
        verbose_name="サイトURL",
        blank=True,
        null=True,
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_admin = models.BooleanField(
        default=False
    )

    objects = UserManager()

    REQUIRED_FIELDS = ['company_name', 'name']
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def is_staff(self):
        return self.is_admin

    def get_fullname(self):
        if self.company_name:
            return self.company_name + " " + self.name
        else:
            return self.name

    def __str__(self):
        return self.get_fullname()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def has_payjp_customer(self):
        try:
            _ = self.payjpinfo
            return True
        except ObjectDoesNotExist:
            return False

    def has_payjp_customer_id(self):
        # TODO: validate with regular expression.
        try:
            _ = self.payjpinfo
            if _.customer_id:
                return True
            return False
        except ObjectDoesNotExist:
            return False

    def get_default_delivery_address(self):
        return self.deliveryaddress_set.filter(is_default=True).first()

    def get_default_billing_address(self):
        return self.billingaddress_set.filter(is_default=True).first()

    def change_default_delivery_address(self, address):
        self.deliveryaddress_set.filter(is_default=True).update(is_default=False)
        address.is_default = True
        address.save()
        return address

    def change_default_billing_address(self, address):
        self.billingaddress_set.filter(is_default=True).update(is_default=False)
        address.is_default = True
        address.save()
        return address


class PayJPInfo(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    customer_id = models.CharField(
        max_length=64
    )


class DeliveryAddress(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=120
    )

    postal_code = models.CharField(
        max_length=12,
        validators=[validate_postal_code],
    )

    prefecture = models.CharField(
        max_length=12,
        choices=PREFECTURES
    )

    city = models.CharField(
        max_length=120
    )

    building = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    tel = models.CharField(
        max_length=36,
        validators=[validate_tel],
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    last_used = models.DateTimeField(
        auto_now=True
    )

    is_default = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.get_full_name() + ": " + self.get_full_address()

    def get_full_address(self):
        if self.building:
            return self.prefecture + self.city + self.building
        return self.prefecture + self.city

    def get_address_with_prefecture(self):
        if self.building:
            return self.city + self.building
        return self.city

    def get_full_name(self):
        # add prefix and return full name
        return "".join([str(_) for _ in [self.name, ] if _])


class BillingAddress(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=120
    )

    postal_code = models.CharField(
        max_length=12,
        validators=[validate_postal_code],
    )

    prefecture = models.CharField(
        max_length=12,
        choices=PREFECTURES
    )

    city = models.CharField(
        max_length=120
    )

    building = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    tel = models.CharField(
        max_length=36,
        validators=[validate_tel],
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    last_used = models.DateTimeField(
        auto_now=True
    )

    is_default = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.get_full_name() + ": " + self.get_full_address()

    def get_full_address(self):
        return "".join([str(_) for _ in [self.prefecture, self.city, self.building] if _])

    def get_address_with_prefecture(self):
        return "".join([str(_) for _ in [self.city, self.building] if _])

    def get_full_name(self):
        # add prefix and return full name
        return "".join([str(_) for _ in [self.name, ] if _])


def post_save_user(sender, instance, **kwargs):
    if not instance.has_payjp_customer():
        customer_id = payjp_create_customer(instance.get_fullname())
        PayJPInfo.objects.create(
            user=instance,
            customer_id=customer_id
        )
        logger.info("Created payjp customer for a user with email:{}, name:{}.".format(instance.email, instance.name))


post_save.connect(post_save_user, sender=User)
