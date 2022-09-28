import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from online_cinema.cast.tests.factories import PersonFactory

from ..models import Card, Country, Episode, Genre, Membership, Season


class CountryFactory(DjangoModelFactory):
    class Meta:
        model = Country

    name = "Russia"


class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = "drama"


class CardFactory(DjangoModelFactory):
    class Meta:
        model = Card

    name = "FilmOrSeries"
    description = "La la la"
    country = factory.SubFactory(CountryFactory)
    is_available = False
    released_year = "2022-03-10"
    banner = "/"

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for genre in extracted:
                self.genres.add(genre)


class MembershipFactory(DjangoModelFactory):
    class Meta:
        model = Membership

    character = "Iron Man"
    item = factory.SubFactory(CardFactory)
    person = factory.SubFactory(PersonFactory)


class PersonWithCardFactory(PersonFactory):
    membership = factory.RelatedFactory(
        MembershipFactory,
        factory_related_name="person",
    )


class CardWithPersonFactory(CardFactory):
    cast = factory.RelatedFactory(MembershipFactory, factory_related_name="item")


class SeasonFactory(DjangoModelFactory):
    class Meta:
        model = Season

    name = factory.Sequence(lambda n: "Season #%s" % n)
    card = factory.SubFactory(CardFactory)


class EpisodeFactory(DjangoModelFactory):
    class Meta:
        model = Episode

    season = factory.SubFactory(SeasonFactory)
    num = 1
    name = "Episode name"
    preview = "/"
    description = "la la la"
    viewers = 0
    updated_to = factory.LazyFunction(timezone.now)
