import factory
from factory.django import DjangoModelFactory

from ..models import Person


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    firstname = "Adam"
    lastname = "Doe"
    picture = "/pictures"
