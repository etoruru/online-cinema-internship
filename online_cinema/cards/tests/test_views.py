from rest_framework import status
from rest_framework.reverse import reverse
from utils.test_api import CustomTestCase

from ..views import (
    CardViewSet,
    CountryViewSet,
    EpisodeViewSet,
    GenreViewSet,
    SeasonViewSet,
)
from .factories import (
    CardFactory,
    CountryFactory,
    EpisodeFactory,
    GenreFactory,
    SeasonFactory,
)


class CountryTestCase(CustomTestCase):
    def setUp(self):
        CountryFactory.create_batch(5)

    def test_get_list(self):
        url = reverse("cards:country-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one(self):
        url = reverse("cards:country-detail", kwargs={"pk": "1"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


#
# class GenreTestCase(CustomTestCase):
#     def setUp(self):
#         GenreFactory.create_batch(5)
#
#     def test_get_list(self):
#         return self.get_all('cards:genre-list')
#
#
#     def test_get_one(self):
#         url = reverse('cards:genre-detail', kwargs={'pk': '1'})
#         view = GenreViewSet.as_view({'get': 'retrieve'})
#         request = self.factory_request.get(url)
#         response = view(request, pk=1)
#         response.render()
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#
#
# class CardTestCase(CustomTestCase):
#     def setUp(self):
#         CardFactory.create_batch(5)
#
#     def test_get_list(self):
#         url = reverse('cards:card-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_one(self):
#         url = reverse('cards:card-detail', kwargs={'pk': '1'})
#         view = CardViewSet.as_view({'get': 'retrieve'})
#         request = self.factory_request.get(url)
#         response = view(request, pk=1)
#         response.render()
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#
#
# class SeasonTestCase(CustomTestCase):
#     def setUp(self):
#         SeasonFactory.create_batch(5)
#
#     def test_get_list(self):
#         url = reverse('cards:season-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_one(self):
#         url = reverse('cards:season-detail', kwargs={'pk': '1'})
#         view = SeasonViewSet.as_view({'get': 'retrieve'})
#         request = self.factory_request.get(url)
#         response = view(request, pk=1)
#         response.render()
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#
#
# class EpisodeTestCase(CustomTestCase):
#     def setUp(self):
#         EpisodeFactory.create_batch(5)
#
#     def test_get_list(self):
#         url = reverse('cards:episode-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_one(self):
#         url = reverse('cards:episode-detail', kwargs={'pk': '1'})
#         view = EpisodeViewSet.as_view({'get': 'retrieve'})
#         request = self.factory_request.get(url)
#         response = view(request, pk=1)
#         response.render()
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
