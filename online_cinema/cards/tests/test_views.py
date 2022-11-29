import factory
from rest_framework import status
from rest_framework.reverse import reverse

from online_cinema.cast.tests.test_views import PersonFactory
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

    def test_401_unauthorized_user(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED, response.data
        )


class CardTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        CardFactory.create_batch(5)
        PersonFactory.create_batch(3)
        cls.country = CountryFactory.create()
        cls.genre = GenreFactory.create()
        cls.url = reverse("cards:cards-list")

    def test_200_authorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_200_get_one(self):
        card = CardFactory()
        response = self.client.get(self.url, {"pk": card.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_card(self):
        new_card = factory.build(
            dict,
            FACTORY_CLASS=CardFactory,
            country=self.country.pk,
            cast=[{"character": "Captain", "person": 1}],
            genres=[self.genre.pk],
        )
        response = self.client.post(self.url, new_card)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST, response.data
        )

    def test_401_create_card(self):
        new_card = factory.build(
            dict,
            FACTORY_CLASS=CardFactory,
            country=self.country.pk,
            genres=[self.genre.pk],
            # cast=[{"character": "Captain", "person": 3}],
        )
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, new_card)
        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED, response.data
        )

    def test_204_delete_card(self):
        card = CardFactory()
        url = reverse("cards:cards-detail", args=[card.pk])
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )

    def test_401_delete_card(self):
        card = CardFactory()
        url = reverse("cards:cards-detail", args=[card.pk])
        self.client.force_authenticate(user=None)
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED, response.data
        )


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
        season = SeasonFactory()
        response = self.client.get(self.url, {"pk": season.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_season(self):
        new_season = factory.build(dict, FACTORY_CLASS=SeasonFactory, card=self.card.pk)
        response = self.client.post(self.url, new_season)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_403__not_access_create_season(self):
        self.user.groups.clear()
        self.user.save()
        new_season = factory.build(dict, FACTORY_CLASS=SeasonFactory, card=self.card.pk)
        response = self.client.post(self.url, new_season)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_204_delete_season(self):
        season = SeasonFactory()
        url = reverse("cards:season-detail", args=[season.pk])
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )


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
        episode = EpisodeFactory()
        response = self.client.get(self.url, {"pk": episode.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_episode(self):
        new_episode = factory.build(
            dict, FACTORY_CLASS=EpisodeFactory, season=self.season.pk
        )
        response = self.client.post(self.url, new_episode)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_403_denied_create_episode(self):
        self.user.groups.clear()
        self.user.save()
        new_episode = factory.build(
            dict, FACTORY_CLASS=EpisodeFactory, season=self.season.pk
        )
        response = self.client.post(self.url, new_episode)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_204_delete_episode(self):
        episode = EpisodeFactory()
        url = reverse("cards:episode-detail", args=[episode.pk])
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )

    def test_401_delete_episode(self):
        episode = EpisodeFactory()
        url = reverse("cards:episode-detail", args=[episode.pk])
        self.client.force_authenticate(user=None)
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED, response.data
        )
