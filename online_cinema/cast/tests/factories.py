import factory
from factory.django import DjangoModelFactory

from ..models import Person


class PersonFactory(DjangoModelFactory):
    firstname = factory.Faker("first_name")
    lastname = factory.Faker("last_name")
    picture = "/pictures"

    class Meta:
        model = Person
