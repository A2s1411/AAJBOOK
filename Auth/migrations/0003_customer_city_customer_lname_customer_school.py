# Generated by Django 5.0.6 on 2024-06-22 17:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_remove_customer_city_remove_customer_lname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='lname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='school',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
