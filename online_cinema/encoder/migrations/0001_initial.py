# Generated by Django 3.2.15 on 2022-11-15 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_file_path', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('LD', 'loading'), ('RD', 'ready'), ('WT', 'waiting'), ('ENCD', 'encoding')], default='LD', max_length=4)),
                ('file_format', models.CharField(default=None, max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='cards.episode')),
            ],
        ),
        migrations.CreateModel(
            name='ConvertTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_path', models.CharField(max_length=200)),
                ('file_format', models.CharField(max_length=100)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convert_tasks', to='encoder.video')),
            ],
        ),
    ]
