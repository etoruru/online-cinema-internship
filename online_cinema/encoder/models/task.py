from django.db import models

from config.settings import base


class ConvertTask(models.Model):
    output = models.FileField()
    video = models.ForeignKey(
        "Video", on_delete=models.CASCADE, related_name="convert_tasks"
    )
    created_by = models.ForeignKey(
        base.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="tasks"
    )
