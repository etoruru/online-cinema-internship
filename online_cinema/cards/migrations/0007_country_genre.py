from django.db import migrations
import json
import os
from pathlib import Path


def create_country(apps, schema_editor):
    Country = apps.get_model('cards', 'Country')
    db_alias = schema_editor.connection.alias

    with open(os.path.join('/app/initial_data', 'countries.json'), 'r') as f:
        countries = json.load(f)

    Country.objects.using(db_alias).bulk_create([
        Country(**country) for country in countries
    ])


def create_genre(apps, schema_editor):
    Genre = apps.get_model('cards', 'Genre')
    db_alias = schema_editor.connection.alias

    with open('app/initial_data/genres.json', 'r') as f:
        genres = json.load(f)

    Genre.objects.using(db_alias).bulk_create([
        Genre(**genre)for genre in genres
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20220919_0832'),
    ]

    operations = [
        migrations.RunPython(create_country, create_genre, migrations.RunPython.noop)
    ]
