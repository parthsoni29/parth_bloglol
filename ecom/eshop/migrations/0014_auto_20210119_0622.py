# Generated by Django 2.2.14 on 2021-01-19 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0013_auto_20210118_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
