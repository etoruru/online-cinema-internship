# Generated by Django 3.2.15 on 2022-09-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20220913_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='type',
            field=models.CharField(choices=[('F', 'film'), ('S', 'series')], default='F', max_length=1),
            preserve_default=False,
        ),
    ]