# Generated by Django 2.0.6 on 2020-02-08 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pancakes_app', '0002_auto_20200208_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
