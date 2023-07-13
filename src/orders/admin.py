from django.contrib import admin
from .models import (
    Order,
    OrderDeliveryAddress,
    OrderBillingAddress,
    OrderItem,
    OrderItemDesign,
    ProvisionalOrderItemDesign,
    OrderItemDelivery
)
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import reverse


class OrderDeliveryAddressInline(admin.StackedInline):

    model = OrderDeliveryAddress


class OrderBillingAddressInline(admin.StackedInline):

    model = OrderBillingAddress


class OrderItemInline(admin.TabularInline):

    model = OrderItem
    extra = 0
    readonly_fields = ('item_link',)

    def item_link(self, instance):
        return format_html(
            mark_safe('<a href="{}">link to item</a>'.format(
                    reverse("admin:orders_orderitem_change", args=(instance.pk,)),
            ))
        )

    item_link.short_description = "Item"


class OrderItemDeliveryInline(admin.StackedInline):

    model = OrderItemDelivery
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'user', 'state', 'created_at', 'is_charged', )
    inlines = (
        OrderDeliveryAddressInline,
        OrderBillingAddressInline,
        OrderItemInline,
    )


class OrderDesignInline(admin.TabularInline):

    model = OrderItemDesign


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'ref_code', 'created_at']
    readonly_fields = ['quantity', 'prices']
    inlines = (OrderDesignInline, OrderItemDeliveryInline,)


@admin.register(ProvisionalOrderItemDesign)
class ProvisionalOrderItemDesignAdmin(admin.ModelAdmin):
    pass
