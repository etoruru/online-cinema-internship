import factory
from django.utils import timezone
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from online_cinema.cast.tests.factories import PersonFactory

from ..models import Card, Country, Episode, Genre, Membership, Season


class CountryFactory(DjangoModelFactory):
    name = factory.Faker("country")

    class Meta:
        model = Country


class GenreFactory(DjangoModelFactory):
    name = "drama"

    class Meta:
        model = Genre


class CardFactory(DjangoModelFactory):
    type = FuzzyChoice(["F", "S"])
    name = factory.Faker("company")
    description = factory.Faker("text")
    country = factory.SubFactory(CountryFactory)
    is_available = factory.Faker("pybool")
    released_year = factory.Faker("date_of_birth")
    banner = "/"

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if extracted:
            for genre in extracted:
                self.genres.add(genre)

    @factory.post_generation
    def cast(self, create, extracted, **kwargs):
        if extracted:
            for membership in extracted:
                self.cast.add(membership)

    class Meta:
        model = Card


class MembershipFactory(DjangoModelFactory):
    character = factory.Faker("name")
    item = factory.SubFactory(CardFactory)
    person = factory.SubFactory(PersonFactory)

    class Meta:
        model = Membership


class PersonWithCardFactory(PersonFactory):
    membership = factory.RelatedFactory(
        MembershipFactory,
        factory_related_name="person",
    )


class CardWithPersonFactory(CardFactory):
    cast = factory.RelatedFactory(MembershipFactory, factory_related_name="item")


class SeasonFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: "Season #%s" % n)
    card = factory.SubFactory(CardFactory)

    class Meta:
        model = Season


class EpisodeFactory(DjangoModelFactory):
    season = factory.SubFactory(SeasonFactory)
    num = 1
    name = "Episode name"
    preview = "/"
    description = factory.Faker("text")
    viewers = 0
    updated_to = factory.LazyFunction(timezone.now)

    class Meta:
        model = Episode
