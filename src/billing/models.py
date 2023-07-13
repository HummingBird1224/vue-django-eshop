from django.db import models
from django.contrib.auth import get_user_model
from django_mysql import models as mysql_model
from orders.models import Order


User = get_user_model()


class Transaction(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    type = models.CharField(
        max_length=120,
        choices=(('credit_card', 'クレジットカード'),
                 ('bank_transfer', '銀行振込')),
        blank=True,
        null=True
    )

    token = models.CharField(
        max_length=120,
        editable=False,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    extra_info = mysql_model.JSONField(
        null=True,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        editable=False,
    )

    card = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        editable=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    success = models.BooleanField(default=True)

    is_captured = models.BooleanField(default=False)

    def __str__(self):
        return self.token

    class Meta:
        ordering = ['-created_at']
