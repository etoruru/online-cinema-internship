import factory
from rest_framework import status
from rest_framework.reverse import reverse
from utils.test_api import ApiTestCaseWithUser

from online_cinema.cards.tests.factories import CardFactory, EpisodeFactory

from .factories import BookmarkFactory, CommentFactory, HistoryFactory, SubsFactory


class CommentsTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        CommentFactory.create_batch(5)
        cls.episode = EpisodeFactory.create()
        cls.url = reverse("comments:comment-list")

    def test_200_authorized_user(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_200_get_one_comment(self):
        comment = CommentFactory()
        pk = {"pk": comment.pk}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_comment(self):
        new_comment = factory.build(dict, FACTORY_CLASS=CommentFactory)
        new_comment["episode"] = self.episode.pk
        response = self.client.post(self.url, new_comment)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_204_delete_comment(self):
        comment = CommentFactory()
        self.url = reverse("comments:comment-detail", args=[comment.pk])
        self.client.force_authenticate(user=comment.user)
        response = self.client.delete(
            self.url,
        )
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )

    def test_403_forbidden_delete_comment(self):
        comment = CommentFactory()
        self.url = reverse("comments:comment-detail", args=[comment.pk])
        response = self.client.delete(
            self.url,
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)


class BookmarkTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.card = CardFactory.create()
        BookmarkFactory.create_batch(5)
        cls.url = reverse("comments:bookmark-list")

    def test_200_authorized_user(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_200_get_one_bookmark(self):
        bookmark = BookmarkFactory()
        pk = {"pk": bookmark.pk}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_bookmark(self):
        new_bookmark = factory.build(dict, FACTORY_CLASS=BookmarkFactory)
        new_bookmark["card"] = self.card.pk
        response = self.client.post(self.url, new_bookmark)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_204_delete_bookmark(self):
        bookmark = BookmarkFactory()
        url = reverse("comments:bookmark-detail", args=[bookmark.pk])
        self.client.force_authenticate(user=bookmark.user)
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )

    def test_403_forbidden_delete_bookmark(self):
        bookmark = BookmarkFactory()
        url = reverse("comments:bookmark-detail", args=[bookmark.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)


class HistoryTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        HistoryFactory.create_batch(5)
        cls.episode = EpisodeFactory.create()
        cls.url = reverse("comments:history-list")

    def test_200_authorized_user(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_200_get_one_history(self):
        history = HistoryFactory()
        pk = {"pk": history.pk}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_204_delete_history(self):
        history = HistoryFactory()
        url = reverse("comments:history-detail", args=[history.pk])
        self.client.force_authenticate(user=history.user)
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )

    def test_403_forbidden_delete_history(self):
        history = HistoryFactory()
        url = reverse("comments:history-detail", args=[history.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_201_create_history(self):
        new_history = factory.build(dict, FACTORY_CLASS=HistoryFactory)
        new_history["episode"] = self.episode.pk
        response = self.client.post(self.url, new_history)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)


class SubscriptionTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        SubsFactory.create_batch(5)
        cls.url = reverse("comments:subscription-list")

    def test_200_authorized_user(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_200_get_one_sub(self):
        sub = SubsFactory()
        pk = {"pk": sub.pk}
        response = self.client.get(self.url, pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_201_create_sub(self):
        new_sub = factory.build(dict, FACTORY_CLASS=SubsFactory)
        response = self.client.post(self.url, new_sub)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_403_delete_sub(self):
        sub = SubsFactory()
        url = reverse("comments:subscription-detail", args=[sub.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_204_delete_sub(self):
        sub = SubsFactory()
        url = reverse("comments:subscription-detail", args=[sub.pk])
        self.client.force_authenticate(user=sub.user)
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )
