import os
import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from config.settings import base


def _make_directories():
    uid = str(uuid.uuid4())
    first_dir, _ = uid.split("-", maxsplit=1)
    filepath = os.path.join(base.MEDIA_DIR, "videofiles")
    os.makedirs(filepath)
    return filepath


class Video(models.Model):
    class VideoStatus(models.TextChoices):
        LOADING = "LD", _("loading")
        READY = "RD", _("ready")
        WAITING = "WT", _("waiting")
        ENCODING = "ENCD", _("encoding")

    filename = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200)
    # videofile = models.FileField(upload_to=_make_directories)
    created_by = models.ForeignKey(
        base.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="videos"
    )
    item = models.ForeignKey(
        "cards.Episode", on_delete=models.CASCADE, related_name="videos"
    )
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        choices=VideoStatus.choices, default=VideoStatus.LOADING, max_length=4
    )
    resolution = models.CharField(max_length=100, default=None)
