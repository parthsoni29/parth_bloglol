# Generated by Django 3.0.7 on 2020-12-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0003_remove_product_product_brands'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ManyToManyField(blank=True, default='', to='eshop.Category'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_sub_category',
        ),
        migrations.AddField(
            model_name='product',
            name='product_sub_category',
            field=models.ManyToManyField(blank=True, default='', to='eshop.Sub_category'),
        ),
    ]