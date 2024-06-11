from datetime import timedelta

import pendulum
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from fml_api.models import Artist
from fml_api.models import MusicGenre
from fml_api.models import Song


class SongsAPIV1Tests(APITestCase):
    fixtures = ["api_v1_test.json"]

    def setUp(self):
        super().setUp()
        self.artist = Artist.objects.get(pk="3ad4a4c5-67a5-4ad7-a6b4-c1234567890d")
        self.genre = MusicGenre.objects.get(pk="1ad4a4c5-67a5-4ad7-a6b4-a1234567890b")
        self.song = Song.objects.get(pk="4ad4a4c5-67a5-4ad7-a6b4-d1234567890e")
        self.song_2 = Song.objects.get(pk="5ad4a4c5-67a5-4ad7-a6b4-e1234567890f")
        self.songs_url = reverse("song-detail", kwargs={"pk": self.song.pk})

    def test_create_song(self):
        url = reverse("song-list")
        data = {
            "title": "New Song",
            "artist": self.artist.pk,
            "release_date": pendulum.now(),
            "length": "00:03:00",
            "genre": self.genre.pk,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.count(), 3)
        obj = Song.objects.get(pk=response.data["id"])
        self.assertEqual(obj.title, "New Song")
        self.assertEqual(obj.artist.id, self.artist.id)
        self.assertEqual(obj.release_date, data["release_date"])
        self.assertEqual(obj.genre.id, self.genre.id)
        self.assertEqual(obj.length, timedelta(minutes=3))
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_get_song(self):
        response = self.client.get(self.songs_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.song.title)
        self.assertEqual(response.data["artist"], self.artist.id)
        self.assertEqual(response.data["genre"], self.genre.id)

    def test_list_songs(self):
        url = reverse("song-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 2)
        self.assertEqual(response.data["data"][0]["id"], str(self.song.id))
        self.assertEqual(response.data["data"][1]["id"], str(self.song_2.id))

    def test_update_song(self):
        data = {"title": "Updated Song Title"}
        response = self.client.patch(self.songs_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.song.refresh_from_db()
        self.assertEqual(self.song.title, "Updated Song Title")

    def test_delete_song(self):
        response = self.client.delete(self.songs_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Song.objects.count(), 1)
