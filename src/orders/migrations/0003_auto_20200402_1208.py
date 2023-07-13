# Generated by Django 2.2.1 on 2020-04-02 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_shipping_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderbillingaddress',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='orderdeliveryaddress',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='orderitemdelivery',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
