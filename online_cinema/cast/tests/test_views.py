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

    def test_403_not_access(self):
        self.user.groups.clear()
        self.user.save()
        new_person = {"firstname": "Johny", "lastname": "Cool", "picture": "/pictures"}
        response = self.client.post(self.url, new_person)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_201_create_person(self):
        new_person = {"firstname": "Johny", "lastname": "Cool", "picture": "/pictures"}
        response = self.client.post(self.url, new_person)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_200_get_one_person(self):
        pk = {"pk": "1"}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
