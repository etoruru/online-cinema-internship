from rest_framework import status
from rest_framework.reverse import reverse
from utils.test_api import ApiTestCaseWithUser

from online_cinema.cards.tests.factories import CardFactory, EpisodeFactory

from .factories import BookmarkFactory, CommentFactory, HistoryFactory


class CommentsTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        CommentFactory.create_batch(5)
        cls.episode = EpisodeFactory.create()
        cls.url = reverse("comments:comment-list")

    def test_200_authorized_user(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_200_get_one_comment(self):
        pk = {"pk": "1"}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_comment(self):
        new_comment = {
            "text": "My comment",
            "created_at": "2022-09-13T11:29:50Z",
            "user": self.user,
            "episode": self.episode,
        }
        response = self.client.post(self.url, new_comment)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)


class BookmarkTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.card = CardFactory.create()
        BookmarkFactory.create_batch(5)
        cls.url = reverse("comments:bookmark-list")

    def test_200_authorized_user(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_200_get_one_bookmark(self):
        pk = {"pk": "1"}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_bookmark(self):
        new_bookmark = {"user": self.user, "card": self.card.pk}
        response = self.client.post(self.url, new_bookmark)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)


class HistoryTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        HistoryFactory.create_batch(5)
        cls.url = reverse("comments:history-list")

    def test_200_authorized_user(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_200_get_one_history(self):
        pk = {"pk": "1"}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
