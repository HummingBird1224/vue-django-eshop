# Generated by Django 3.1.3 on 2021-03-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_productprice_sample_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprice',
            name='sample_unit_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
