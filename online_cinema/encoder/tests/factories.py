import factory
from factory.django import DjangoModelFactory

from ..models import Video


class VideoFactory(DjangoModelFactory):
    class Meta:
        model = Video
