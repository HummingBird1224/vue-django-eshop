from django.contrib import admin
from .models import (NoticeCategory,
                     NoticePost,
                     NoticeReminder)


@admin.register(NoticeCategory)
class NoticeCategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'message', 'icon_path']


@admin.register(NoticePost)
class NoticePostAdmin(admin.ModelAdmin):

    list_display = ['post_title', 'created_at', 'last_edited_at', 'published_at']


@admin.register(NoticeReminder)
class NoticeReminderAdmin(admin.ModelAdmin):

    list_display = ['category', 'orderitem']
