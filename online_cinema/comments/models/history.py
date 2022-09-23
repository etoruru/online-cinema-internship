from cards.models import Episode
from django.db import models
from django.utils import timezone

from config.settings import base


class History(models.Model):
    date_visited = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="history"
    )
    episode = models.ForeignKey(
        Episode, on_delete=models.CASCADE, related_name="history"
    )
