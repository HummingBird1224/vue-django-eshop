# Generated by Django 2.2.1 on 2020-04-02 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200402_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='last_name',
        ),
    ]
