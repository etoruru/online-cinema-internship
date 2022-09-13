# Generated by Django 3.2.15 on 2022-09-13 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20220913_1134'),
        ('encoder', '0004_auto_20220913_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trailers', to='cards.card'),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trailers', to='encoder.video'),
        ),
    ]
