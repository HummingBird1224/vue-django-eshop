from datetime import datetime
from django.db import models
from django.utils import timezone
from billing.models import Transaction
from orders.models import OrderItem
from django.db import transaction
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

User = get_user_model()

def get_notice_category_icon_image_path(instance, filename):
    prefix = 'notices/category/icons/'
    return prefix + filename

class NoticeCategory(models.Model):

    name = models.CharField(max_length=255)

    message = models.CharField(max_length=255)

    slug = models.SlugField(
        blank=True,
        null=True
    )

    icon_path = models.FileField(
        upload_to=get_notice_category_icon_image_path,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'svg'])],
    )

    post_attachable = models.BooleanField(default=False)

    def __str__(self):
        return self.message


class Notice(models.Model):
    category = models.ForeignKey(
        NoticeCategory,
        on_delete=models.PROTECT
    )

    users = models.ManyToManyField(
        User,
        through='NoticeRead',
    )

    created_at = models.DateTimeField(default=timezone.now)

class NoticePost(Notice):

    post_title = models.CharField(max_length=120, default='canalからのお知らせ')

    text = models.TextField()

    last_edited_at = models.DateTimeField(auto_now=True)

    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.post_title

class NoticeReminder(Notice):
    
    orderitem = models.ForeignKey(
        OrderItem,
        on_delete=models.CASCADE,
        max_length=255
    )

class NoticeRead(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    notices = models.ForeignKey(Notice, on_delete=models.CASCADE)

    read_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

def create_data_import_notice(sender, instance, created, **kwargs):
    # デザインデータ再入稿依頼の場合、もしくはN日後にread=1でもデータ入稿が完了していない場合、再度作成する
    if created:
        category = NoticeCategory.objects.get(name='data import reminder')
        for item in instance.order.items.all():
            NoticeReminder.objects.create(notice_ptr=None,orderitem=item, category_id=category.id)

def attach_reminder_to_user(sender, instance, created, **kwargs):
    if created:
        instance.notice_ptr.users.add(instance.orderitem.order.user)

post_save.connect(create_data_import_notice, sender=Transaction)
post_save.connect(attach_reminder_to_user, sender=NoticeReminder)
