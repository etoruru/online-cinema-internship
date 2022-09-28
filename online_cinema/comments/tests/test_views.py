from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from utils.test_api import CustomTestCase

# from .factories import AdminFactory
from online_cinema.users.tests.factories import UserFactory

from ..views import CommentViewSet


class CommentsTestCase(CustomTestCase):
    def test_get_list(self):
        url = reverse("comments:comment-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one(self):
        url = reverse("comments:comment-detail", kwargs={"pk": "1"})
        view = CommentViewSet.as_view({"get": "retrieve"})
        request = self.factory_request.get(url)
        response = view(request, pk=1)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookmarkTestCase(CustomTestCase):
    def test_get_list(self):
        url = reverse("comments:bookmark-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one(self):

        # url = reverse('comments:bookmark-detail', kwargs={'pk': '1'})
        # view = CommentViewSet.as_view({'get': 'retrieve'})
        request = self.client.get("/bookmarks/1/")
        # response = view(request, pk=1)
        # response.render()
        self.assertEqual(request.user, status.HTTP_200_OK)


class HistoryTestCase(CustomTestCase):
    def test_get_list(self):
        url = reverse("comments:history-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
