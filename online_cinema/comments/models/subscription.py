from django.db import models

from config.settings import base


class Subscription(models.Model):
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscription"
    )
    expired_date = models.DateTimeField()
