import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from online_cinema.cards.tests.factories import CardFactory, EpisodeFactory
from online_cinema.users.tests.factories import UserFactory

from ..models import Trailer, Video


class VideoFactory(DjangoModelFactory):
    filename = factory.Sequence(lambda n: "video #%s" % n)
    filepath = "/videos"
    created_by = factory.SubFactory(UserFactory)
    item = factory.SubFactory(EpisodeFactory)
    resolution = "720"
    created_at = factory.LazyFunction(timezone.now)
    status = "WT"

    class Meta:
        model = Video


class TrailerFactory(DjangoModelFactory):
    resolution = "720"
    card = factory.SubFactory(CardFactory)
    video = factory.SubFactory(VideoFactory)

    class Meta:
        model = Trailer
