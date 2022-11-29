import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from config.settings import base
from online_cinema.cards.tests.factories import CardFactory, EpisodeFactory
from online_cinema.users.tests.factories import UserFactory

from ..models import ConvertTask, Video


class VideoFactory(DjangoModelFactory):
    source_file_path = "{}/{}".format(
        base.MEDIA_ROOT, factory.Sequence(lambda n: "video#%s.mp4" % n)
    )
    created_by = factory.SubFactory(UserFactory)
    item = factory.SubFactory(EpisodeFactory)
    file_format = "mp4"
    created_at = factory.LazyFunction(timezone.now)
    status = "WT"

    class Meta:
        model = Video


class TaskFactory(DjangoModelFactory):
    output = base.MEDIA_ROOT
    created_by = factory.SubFactory(UserFactory)
    video = factory.SubFactory(VideoFactory)

    class Meta:
        model = ConvertTask
