# Generated by Django 3.2.15 on 2022-11-28 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('encoder', '0003_remove_converttask_file_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='converttask',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='users.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='converttask',
            name='output',
            field=models.CharField(max_length=200),
        ),
    ]