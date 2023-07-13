# Generated by Django 3.1.3 on 2023-04-26 17:35

import casestudies.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # ('products', '0031_auto_20230426_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('overview', models.TextField(blank=True, max_length=500, null=True, verbose_name='説明文')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=casestudies.models.get_casestudy_category_icon_path, verbose_name='アイコン')),
                ('image', models.ImageField(blank=True, null=True, upload_to=casestudies.models.get_casestudy_category_image_path, verbose_name='画像')),
                ('URL', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('position', models.PositiveSmallIntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='casestudies.casestudycategory', verbose_name='商品区分')),
            ],
        ),
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('client', models.CharField(max_length=255, verbose_name='顧客名')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('text', models.TextField(blank=True, max_length=500, null=True, verbose_name='説明文')),
                ('image', models.ImageField(blank=True, null=True, upload_to=casestudies.models.get_casestudy_image_path, verbose_name='画像')),
                ('position', models.PositiveSmallIntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('material', models.ManyToManyField(blank=True, related_name='material', to='casestudies.CaseStudyCategory', verbose_name='材質')),
                ('printing_method', models.ManyToManyField(blank=True, related_name='printing_method', to='casestudies.CaseStudyCategory', verbose_name='印刷方法')),
                ('processing', models.ManyToManyField(blank=True, related_name='processing', to='casestudies.CaseStudyCategory', verbose_name='加工')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='商品')),
                ('product_category', models.ManyToManyField(blank=True,related_name='product_category', to='casestudies.CaseStudyCategory', verbose_name='商品区分')),
                ('shape', models.ManyToManyField(blank=True, related_name='shape', to='casestudies.CaseStudyCategory', verbose_name='形状')),
                ('sustainability', models.ManyToManyField(blank=True, related_name='sustainability', to='casestudies.CaseStudyCategory', verbose_name='環境配慮')),
                ('usage', models.ManyToManyField(blank=True, related_name='usage', to='casestudies.CaseStudyCategory', verbose_name='用途')),
            ],
        ),
    ]
