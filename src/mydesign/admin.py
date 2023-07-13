from django.contrib import admin
from .models import MyDesign, MyDesignDesign


class MyDesignDesignInline(admin.TabularInline):

    model = MyDesignDesign


@admin.register(MyDesign)
class MyDesignAdmin(admin.ModelAdmin):

    list_display = ('user', 'product', 'created_at')
    inlines = (MyDesignDesignInline,)
