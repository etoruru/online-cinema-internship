import factory
from rest_framework import status
from rest_framework.reverse import reverse

from online_cinema.utils.test_api import ApiTestCaseWithUser

from .factories import PersonFactory


class TestCastViewSet(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        PersonFactory.create_batch(5)
        cls.url = reverse("cast:person-list")

    def test_200_authorized_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_403_not_access_create(self):
        self.user.groups.clear()
        self.user.save()
        new_person = factory.build(dict, FACTORY_CLASS=PersonFactory)
        response = self.client.post(self.url, new_person)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_201_create_person(self):
        new_person = factory.build(dict, FACTORY_CLASS=PersonFactory)
        response = self.client.post(self.url, new_person)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_200_get_one_person(self):
        person = PersonFactory()
        pk = {"pk": person.pk}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_204_delete_person(self):
        person = PersonFactory()
        url = reverse("cast:person-detail", args=[person.pk])
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )

    def test_403_delete_person(self):
        self.user.groups.clear()
        self.user.save()
        person = PersonFactory()
        url = reverse("cast:person-detail", args=[person.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)
