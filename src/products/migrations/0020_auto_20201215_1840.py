# Generated by Django 2.2.1 on 2020-12-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_easydraft_easydraftprintarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='easydraft',
            name='pdf_background_color',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='easydraft',
            name='pdf_border_color',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
