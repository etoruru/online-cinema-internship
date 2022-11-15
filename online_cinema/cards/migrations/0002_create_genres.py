
from django.db import migrations
import json
import os
from config.settings import base


def create_genre(apps, schema_editor):
    Genre = apps.get_model('cards', 'Genre')
    db_alias = schema_editor.connection.alias

    with open(os.path.join(base.ROOT_DIR, 'initial_data/genres.json'), 'r') as f:
        genres = json.load(f)

    Genre.objects.using(db_alias).bulk_create([
        Genre(**genre)for genre in genres
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_genre, migrations.RunPython.noop)
    ]
