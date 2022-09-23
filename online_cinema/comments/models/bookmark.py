from django.db import models

from config.settings import base


class Bookmark(models.Model):
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookmark"
    )
    card = models.ForeignKey(
        "cards.Card", on_delete=models.CASCADE, related_name="bookmark"
    )
