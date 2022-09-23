from cards.models import Card
from django.db import models

from .video import Video


class Trailer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="trailers")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="trailers")
    resolution = models.CharField(max_length=100, default=None)
