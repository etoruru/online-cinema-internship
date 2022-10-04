# Generated by Django 3.2.15 on 2022-10-04 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0002_delete_cast'),
        ('cards', '0007_country_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='card_to_person', to='cards.card'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_to_person', to='cast.person'),
        ),
    ]
