from django.db import migrations
import json
import os
from config.settings import base


def create_country(apps, schema_editor):
    Country = apps.get_model('cards', 'Country')
    db_alias = schema_editor.connection.alias

    with open(os.path.join(base.ROOT_DIR, 'initial_data/countries.json'), 'r') as f:
        countries = json.load(f)

    Country.objects.using(db_alias).bulk_create([
        Country(**country) for country in countries
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_create_genres'),
    ]

    operations = [
        migrations.RunPython(create_country, migrations.RunPython.noop),
    ]
