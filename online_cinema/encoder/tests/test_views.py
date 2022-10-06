import factory
from rest_framework import status
from rest_framework.reverse import reverse
from utils.test_api import ApiTestCaseWithUser

from online_cinema.cards.tests.factories import CardFactory, EpisodeFactory

from .factories import TrailerFactory, VideoFactory


class VideoTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        VideoFactory.create_batch(5)
        cls.url = reverse("encoder:video-list")
        cls.episode = EpisodeFactory.create()

    def test_200_admin_user(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_200_get_one_video(self):
        video = VideoFactory()
        response = self.client.get(self.url, {"pk": video.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_204_delete_video(self):
        video = VideoFactory()
        url = reverse("encoder:video-detail", args=[video.pk])
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )

    def test_403_delete_video(self):
        video = VideoFactory()
        url = reverse("encoder:video-detail", args=[video.pk])
        self.client.force_authenticate(user=None)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_201_create_video(self):
        new_video = factory.build(
            dict, FACTORY_CLASS=VideoFactory, item=self.episode.pk
        )
        response = self.client.post(self.url, new_video)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_403_create_video(self):
        new_video = factory.build(
            dict, FACTORY_CLASS=VideoFactory, item=self.episode.pk
        )
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, new_video)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_403_not_admin_user(self):
        self.user.groups.clear()
        self.user.save()
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_403_unauthorized_user(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)


class TrailerTestCase(ApiTestCaseWithUser):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        TrailerFactory.create_batch(5)
        cls.card = CardFactory()
        cls.video = VideoFactory()
        cls.url = reverse("encoder:trailer-list")

    def test_200_admin_user(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_403_not_admin_user(self):
        self.user.groups.clear()
        self.user.save()
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def test_200_get_one_trailer(self):
        trailer = TrailerFactory()
        response = self.client.get(self.url, {"pk": trailer.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_204_delete_trailer(self):
        trailer = TrailerFactory()
        url = reverse("encoder:trailer-detail", args=[trailer.pk])
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT, response.data
        )

    def test_403_delete_trailer(self):
        trailer = TrailerFactory()
        url = reverse("encoder:trailer-detail", args=[trailer.pk])
        self.client.force_authenticate(user=None)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)
