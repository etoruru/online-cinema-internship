from cards.models import Episode
from django.db import models
from django.utils import timezone

from config.settings import base


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    episode = models.ForeignKey(
        Episode, on_delete=models.CASCADE, related_name="comments"
    )
