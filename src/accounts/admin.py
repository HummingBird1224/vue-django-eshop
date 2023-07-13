from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from django.contrib.auth.models import Group
from django.http import HttpResponse
import csv

from .models import *


class PayJPInfoInline(admin.TabularInline):

    model = PayJPInfo


class DeliveryAddressInline(admin.StackedInline):

    model = DeliveryAddress
    extra = 0


class BillingAddressInline(admin.StackedInline):

    model = BillingAddress
    extra = 0


@admin.register(User)
class UserAdmin(UA):
    list_display = ('__str__', 'id', 'company_name', 'email', 'date_joined', 'is_active',)
    list_filter = ()
    inlines = (PayJPInfoInline, DeliveryAddressInline, BillingAddressInline,)
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal Info', {'fields': ('email', 'company_name', 'url', 'extra_info', 'name', 'date_joined', 'updated_at',)}),
        ('Permissions', {'fields': ('is_active', 'is_admin',)}),
    )
    readonly_fields = ('date_joined', 'updated_at',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'company_name', 'name', 'password1', 'password2',),
        }),
    )
    search_fields = ('email', 'company_name', 'name',)
    ordering = ('-date_joined',)
    filter_horizontal = ()
    actions = ["export_as_csv"]

    def add_view(self, request, form_url='', extra_context=None):
        self.inlines = ()
        return super().add_view(request, form_url='', extra_context=None)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url='', extra_context=None)

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields if field.name != 'password']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "選択された ユーザー のCSV出力"


admin.site.unregister(Group)
