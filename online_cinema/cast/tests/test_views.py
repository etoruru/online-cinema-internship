from rest_framework import status
from rest_framework.reverse import reverse
from utils.test_api import CustomTestCase

from .factories import PersonFactory


class CastTestCase(CustomTestCase):
    def setUp(self):
        PersonFactory.create_batch(10)

    def test_get_list(self):
        url = reverse("cast:person-list")
        response = self.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one(self):
        url = reverse("cast:person-detail", kwargs={"pk": "1"})
        response = self.get(url=url, user=self.admin_user)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_person(self):
        url = reverse("cast:person-list")
        response = self.post(
            url,
            {"firstname": "John", "lastname": "Doe", "picture": "/"},
            user=self.admin_user,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
