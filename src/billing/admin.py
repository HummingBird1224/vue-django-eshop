from django.contrib import admin
from .models import Transaction
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import reverse


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = ('user', 'amount', 'order', 'token', 'type', 'is_captured', 'created_at')
    readonly_fields = ('amount', 'token', 'card', 'order_link')
    search_fields = ('token', )

    def order_link(self, instance):
        return format_html(
            mark_safe('<a href="{}">link to order</a>'.format(
                    reverse("admin:orders_order_change", args=(instance.order.pk,)),
            ))
        )

    order_link.short_description = "Order"
