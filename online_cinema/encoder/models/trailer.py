from django.db import models


class Trailer(models.Model):
    card = models.ForeignKey(
        "cards.Card", on_delete=models.CASCADE, related_name="trailers"
    )
    video = models.ForeignKey(
        "Video", on_delete=models.CASCADE, related_name="trailers"
    )
    resolution = models.CharField(max_length=100, default=None)
