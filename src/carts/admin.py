from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):

    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ['user', '__str__', 'created_at', 'last_changed']
    inlines = [CartItemInline, ]



