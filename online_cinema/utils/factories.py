import factory
from django.contrib.auth.models import Group
from factory.django import DjangoModelFactory

from online_cinema.users.tests.factories import UserFactory


class AdminFactory(UserFactory):
    is_staff = True

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.groups.add(extracted)


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = "admin"
