from cards.models import Card, Episode
from django.db import models
from django.utils import timezone

from online_cinema.users.models import User

VIDEO_STATUS = [
    ("LOAD", "loading"),
    ("RD", "ready"),
    ("WT", "waitng"),
    ("ENCD", "encoding"),
]


class Video(models.Model):
    filename = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="video")
    item = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="video")
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=VIDEO_STATUS, max_length=4)


class Trailer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="trailer")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="trailer")
