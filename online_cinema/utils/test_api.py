from rest_framework.test import APITestCase

from online_cinema.users.tests.factories import UserFactory

from .factories import AdminFactory, GroupFactory


class ApiTestCaseWithUser(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = AdminFactory.create()
        cls.user.groups.add(GroupFactory.create())

    def setUp(self) -> None:
        self.client.force_authenticate(self.user)
