import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from online_cinema.cards.tests.factories import CardFactory, EpisodeFactory
from online_cinema.users.tests.factories import UserFactory

from ..models import Bookmark, Comment, History


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    text = "There are some comments!"
    created_at = factory.LazyFunction(timezone.now)
    user = factory.SubFactory(UserFactory)
    episode = factory.SubFactory(EpisodeFactory)


class HistoryFactory(DjangoModelFactory):
    class Meta:
        model = History

    date_visited = factory.LazyFunction(timezone.now)
    user = factory.SubFactory(UserFactory)
    episode = factory.SubFactory(EpisodeFactory)


class BookmarkFactory(DjangoModelFactory):
    class Meta:
        model = Bookmark

    user = factory.SubFactory(UserFactory)
    card = factory.SubFactory(CardFactory)
