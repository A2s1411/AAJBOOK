# Generated by Django 5.0.6 on 2024-06-30 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_member_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='passwd1',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
