import pendulum
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from fml_api.models import Artist
from fml_api.models import MusicGenre
from fml_api.models import Song
from fml_api.models import SongAlbum


class SongAlbumsAPIV1Tests(APITestCase):
    fixtures = ["api_v1_test.json"]

    def setUp(self):
        super().setUp()
        self.artist = Artist.objects.get(pk="3ad4a4c5-67a5-4ad7-a6b4-c1234567890d")
        self.genre = MusicGenre.objects.get(pk="1ad4a4c5-67a5-4ad7-a6b4-a1234567890b")
        self.song = Song.objects.get(pk="4ad4a4c5-67a5-4ad7-a6b4-d1234567890e")
        self.song_2 = Song.objects.get(pk="5ad4a4c5-67a5-4ad7-a6b4-e1234567890f")
        self.song_album = SongAlbum.objects.get(
            pk="6ad4a4c5-67a5-4ad7-a6b4-f12345678901"
        )
        self.song_albums_url = reverse(
            "songalbum-detail", kwargs={"pk": self.song_album.pk}
        )

    def test_create_song_album(self):
        url = reverse("songalbum-list")
        data = {
            "title": "New Song Album",
            "artist": self.artist.pk,
            "release_date": pendulum.now().date(),
            "genre": self.genre.pk,
            "songs": [self.song.pk],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SongAlbum.objects.count(), 2)
        obj = SongAlbum.objects.get(pk=response.data["id"])
        self.assertEqual(obj.title, "New Song Album")
        self.assertEqual(obj.artist.id, self.artist.id)
        self.assertEqual(obj.release_date, data["release_date"])
        self.assertEqual(obj.genre.id, self.genre.id)
        self.assertEqual(obj.songs.get(), self.song)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_get_song_album(self):
        response = self.client.get(self.song_albums_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.song_album.title)
        self.assertEqual(response.data["artist"], self.artist.id)
        self.assertEqual(response.data["genre"], self.genre.id)
        self.assertEqual(response.data["songs"], [self.song.pk, self.song_2.pk])

    def test_list_song_albums(self):
        url = reverse("songalbum-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]["id"], str(self.song_album.id))

    def test_update_song_album(self):
        data = {
            "title": "Updated Song Album Title",
        }
        response = self.client.patch(self.song_albums_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.song_album.refresh_from_db()
        self.assertEqual(self.song_album.title, "Updated Song Album Title")

    def test_delete_song_album(self):
        response = self.client.delete(self.song_albums_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SongAlbum.objects.count(), 0)
