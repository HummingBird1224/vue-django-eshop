# Generated by Django 2.2.1 on 2020-10-19 18:05

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import products.models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_is_reorderable'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_contact_required', models.BooleanField(default=False)),
                ('can_order_sample', models.BooleanField(default=False)),
                ('min_ordering_quantity', models.PositiveIntegerField(default=0)),
                ('max_ordering_quantity', models.PositiveIntegerField(default=0)),
                ('estimated_shipping_date_first', models.PositiveIntegerField(default=0)),
                ('estimated_shipping_date_repeat', models.PositiveIntegerField(default=0)),
                ('can_select_original_size', models.BooleanField(default=False)),
                ('is_design_necessary', models.BooleanField(default=True)),
                ('is_easy_draft_available', models.BooleanField(default=False)),
                ('notes', django_mysql.models.JSONField(blank=True, default=dict, null=True)),
                ('shipping_area', django_mysql.models.JSONField(blank=True, default=dict, null=True)),
                ('size_limit', django_mysql.models.JSONField(blank=True, default=dict, null=True)),
                ('choosable_color', django_mysql.models.JSONField(blank=True, default=dict, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=360)),
                ('detail', models.TextField(blank=True, null=True)),
                ('required', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(default=1)),
                ('widget_type', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='ProductOptionCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOptionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=360, null=True)),
                ('delimiter', models.CharField(blank=True, max_length=8, null=True)),
                ('value', models.CharField(blank=True, max_length=360, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.get_option_item_image_path)),
                ('is_default', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_reorderable', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(default=1)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.ProductOption')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='extra_info',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_reorderable',
        ),
        migrations.RemoveField(
            model_name='productprice',
            name='is_active',
        ),
        migrations.AddField(
            model_name='productimage',
            name='is_hover_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productprice',
            name='refer_to',
            field=models.CharField(choices=[('url', 'url'), ('csv', 'csv')], default='url', max_length=120),
        ),
        migrations.AddField(
            model_name='productprice',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='key',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=120, unique=True, validators=[
                django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'),
                                                      'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.',
                                                      'invalid')]),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(max_length=120, unique=True, validators=[
                django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'),
                                                      'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.',
                                                      'invalid')]),
        ),
        migrations.AlterField(
            model_name='productusecase',
            name='slug',
            field=models.SlugField(max_length=120, unique=True, validators=[
                django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'),
                                                      'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.',
                                                      'invalid')]),
        ),
        migrations.DeleteModel(
            name='ProductThumbnail',
        ),
        migrations.AddField(
            model_name='productoptioncondition',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condition', to='products.ProductOptionItem'),
        ),
        migrations.AddField(
            model_name='productoptioncondition',
            name='values',
            field=models.ManyToManyField(to='products.ProductOptionItem'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='products.Product'),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='products.Product'),
        ),
    ]
