from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from online_cinema.users.tests.factories import UserFactory

# from .factories import AdminFactory
from .factories import AdminFactory, GroupFactory


class CustomTestCase(APITestCase):

    admin_user = AdminFactory.create(groups=1)
    non_admin_user = UserFactory.create()

    def get(self, url, user=None):
        if user:
            self.client.force_authenticate(user)
        response = self.client.get(url)
        return response

    def post(self, url, data, user=None):
        if user:
            self.client.force_authenticate(user)
        return self.client.post(url, data)
