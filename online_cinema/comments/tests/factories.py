import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from online_cinema.cards.tests.factories import CardFactory, EpisodeFactory
from online_cinema.users.tests.factories import UserFactory

from ..models import Bookmark, Comment, History


class CommentFactory(DjangoModelFactory):
    text = "There are some comments!"
    created_at = factory.LazyFunction(timezone.now)
    user = factory.SubFactory(UserFactory)
    episode = factory.SubFactory(EpisodeFactory)

    class Meta:
        model = Comment


class HistoryFactory(DjangoModelFactory):
    date_visited = factory.LazyFunction(timezone.now)
    user = factory.SubFactory(UserFactory)
    episode = factory.SubFactory(EpisodeFactory)

    class Meta:
        model = History


class BookmarkFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    card = factory.SubFactory(CardFactory)

    class Meta:
        model = Bookmark
