from rest_framework import status
from rest_framework.reverse import reverse

from online_cinema.cards.models import Country
from online_cinema.utils.test_api import ApiTestCaseWithUser

from .factories import (
    CardFactory,
    CountryFactory,
    EpisodeFactory,
    GenreFactory,
    SeasonFactory,
)


class CountryTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse("cards:country-list")

    def test_200_authorized_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)


class CardTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        CardFactory.create_batch(5)
        cls.country = Country.objects.filter(30)
        cls.genre = GenreFactory.create()
        cls.url = reverse("cards:card-list")

    def test_200_authorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_200_get_one(self):
        pk = {"pk": "1"}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_card(self):
        new_card = {
            "name": "Blockbaster",
            "type": "F",
            "description": "It' a cool film",
            "released_year": "2022-10-12",
            "country": self.country,
            "banner": "/",
            "is_available": False,
            "genres": [self.genre.pk],
            "cast": [{"character": "Captain", "person": 3}],
        }
        response = self.client.post(self.url, new_card)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)


class SeasonTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        SeasonFactory.create_batch(5)
        cls.card = CardFactory.create()
        cls.url = reverse("cards:season-list")

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_200_get_one(self):
        pk = {"pk": "1"}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_season(self):
        new_season = {"name": "1", "card": self.card.pk}
        response = self.client.post(self.url, new_season)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_403__not_access_create_season(self):
        self.user.groups.clear()
        self.user.save()
        new_season = {"name": "1", "card": self.card.pk}
        response = self.client.post(self.url, new_season)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)


class EpisodeTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        EpisodeFactory.create_batch(5)
        cls.season = SeasonFactory.create()
        cls.url = reverse("cards:episode-list")

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_200_get_one(self):
        pk = {"pk": "1"}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_episode(self):
        new_episode = {
            "num": 3,
            "name": "Red",
            "preview": "/",
            "description": "killeeer",
            "viewers": 0,
            "updated_to": "2022-09-13T11:29:50Z",
            "season": self.season.pk,
        }
        response = self.client.post(self.url, new_episode)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_403_denied_create_episode(self):
        self.user.groups.clear()
        self.user.save()
        new_episode = {
            "num": 3,
            "name": "Red",
            "preview": "/",
            "description": "killeeer",
            "viewers": 0,
            "updated_to": "2022-09-13T11:29:50Z",
            "season": self.season.pk,
        }
        response = self.client.post(self.url, new_episode)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)
