from django.db import models
from django.utils import timezone

from .season import Season


class Episode(models.Model):
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name="episodes"
    )
    num = models.IntegerField(default=1)
    name = models.CharField(max_length=200)
    preview = models.CharField(max_length=200)
    description = models.TextField(default="-")
    viewers = models.IntegerField(default=0)
    updated_to = models.DateTimeField(default=timezone.now)
