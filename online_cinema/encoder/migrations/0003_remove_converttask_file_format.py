# Generated by Django 3.2.15 on 2022-11-21 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encoder', '0002_auto_20221115_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='converttask',
            name='file_format',
        ),
    ]
