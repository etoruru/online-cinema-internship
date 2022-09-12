from cards.models import Card, Episode
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


class History(models.Model):
    date_visited = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="history"
    )
    episode = models.ForeignKey(
        Episode, on_delete=models.CASCADE, related_name="history"
    )


class Bookmark(models.Model):
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookmark"
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="bookmark")


class Subscription(models.Model):
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscription"
    )
    expired_date = models.DateTimeField()
