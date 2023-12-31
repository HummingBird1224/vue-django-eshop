# Generated by Django 3.1.3 on 2021-02-09 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import mydesign.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0023_auto_20210113_1700'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=120, null=True)),
                ('name', models.CharField(blank=True, max_length=360, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('size', django_mysql.models.JSONField(blank=True, default=dict, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=mydesign.models.get_mydesign_image_path)),
                ('read_only_options', django_mysql.models.JSONField(blank=True, default=dict, null=True)),
                ('ordered_num', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
