
# Generated by Django 5.0.6 on 2024-06-22 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_customer_city_customer_lname_customer_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='school',
        ),
    ]
