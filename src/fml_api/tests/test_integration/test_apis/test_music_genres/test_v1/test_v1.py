from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from fml_api.models import MusicGenre


class MusicGenresAPIV1Tests(APITestCase):
    fixtures = ["api_v1_test.json"]

    def setUp(self):
        super().setUp()
        self.genre = MusicGenre.objects.get(pk="1ad4a4c5-67a5-4ad7-a6b4-a1234567890b")
        self.genre_2 = MusicGenre.objects.get(pk="2ad4a4c5-67a5-4ad7-a6b4-b1234567890c")
        self.genres_url = reverse("musicgenre-detail", kwargs={"pk": self.genre.pk})

    def test_create_music_genre(self):
        url = reverse("musicgenre-list")
        data = {"name": "New Genre", "description": "New Description"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MusicGenre.objects.count(), 3)
        obj = MusicGenre.objects.get(pk=response.data["id"])
        self.assertEqual(obj.name, "New Genre")
        self.assertEqual(obj.description, "New Description")
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_get_music_genre(self):
        response = self.client.get(self.genres_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.genre.name)
        self.assertEqual(response.data["description"], self.genre.description)

    def test_list_music_genres(self):
        url = reverse("musicgenre-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 2)
        self.assertEqual(response.data["data"][0]["id"], str(self.genre.id))
        self.assertEqual(response.data["data"][1]["id"], str(self.genre_2.id))

    def test_update_music_genre(self):
        data = {
            "name": "Updated Genre",
            "description": "Updated Description",
        }
        response = self.client.patch(self.genres_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.genre.refresh_from_db()
        self.assertEqual(self.genre.name, "Updated Genre")
        self.assertEqual(self.genre.description, "Updated Description")

    def test_delete_music_genre(self):
        response = self.client.delete(self.genres_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MusicGenre.objects.count(), 1)
