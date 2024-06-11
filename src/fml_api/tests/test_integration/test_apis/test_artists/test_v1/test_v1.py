from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from fml_api.models import Artist
from fml_api.models import Song
from fml_api.models import SongAlbum


class ArtistsAPIV1Tests(APITestCase):
    fixtures = ["api_v1_test.json"]

    def setUp(self):
        super().setUp()
        self.artist = Artist.objects.get(pk="3ad4a4c5-67a5-4ad7-a6b4-c1234567890d")
        self.artist_url = reverse("artist-detail", kwargs={"pk": self.artist.pk})

    def test_create_artist(self):
        url = reverse("artist-list")
        data = {"name": "New Artist", "bio": "New Bio", "country": "New Country"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 2)
        obj = Artist.objects.get(pk=response.data["id"])
        self.assertEqual(obj.name, "New Artist")
        self.assertEqual(obj.bio, "New Bio")
        self.assertEqual(obj.country, "New Country")
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_get_artist(self):
        response = self.client.get(self.artist_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.artist.name)
        self.assertEqual(response.data["bio"], self.artist.bio)
        self.assertEqual(response.data["country"], self.artist.country)

    def test_list_artist(self):
        url = reverse("artist-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]["id"], str(self.artist.id))

    def test_update_artist(self):
        data = {
            "name": "Updated Artist",
            "bio": "Updated Bio",
            "country": "Updated Country",
        }
        response = self.client.patch(self.artist_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.artist.refresh_from_db()
        self.assertEqual(self.artist.name, "Updated Artist")
        self.assertEqual(self.artist.bio, "Updated Bio")
        self.assertEqual(self.artist.country, "Updated Country")

    def test_delete_artist(self):
        response = self.client.delete(self.artist_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artist.objects.count(), 0)


class ArtistSongsTests(APITestCase):
    fixtures = ["api_v1_test.json"]

    def setUp(self):
        super().setUp()
        self.artist = Artist.objects.get(pk="3ad4a4c5-67a5-4ad7-a6b4-c1234567890d")
        self.artist_song_1 = Song.objects.get(pk="4ad4a4c5-67a5-4ad7-a6b4-d1234567890e")
        self.artist_song_2 = Song.objects.get(pk="5ad4a4c5-67a5-4ad7-a6b4-e1234567890f")
        self.songs_url = reverse("artist-songs", kwargs={"artist_id": self.artist.pk})

    def test_get_songs_for_artist(self):
        response = self.client.get(self.songs_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 2)
        self.assertEqual(response.data["data"][0]["title"], self.artist_song_1.title)
        self.assertEqual(response.data["data"][1]["title"], self.artist_song_2.title)


class ArtistSongAlbumsTests(APITestCase):
    fixtures = ["api_v1_test.json"]

    def setUp(self):
        super().setUp()
        self.artist = Artist.objects.get(pk="3ad4a4c5-67a5-4ad7-a6b4-c1234567890d")
        self.artist_song_album = SongAlbum.objects.get(
            pk="6ad4a4c5-67a5-4ad7-a6b4-f12345678901"
        )
        self.song_albums_url = reverse(
            "artist-song-albums", kwargs={"artist_id": self.artist.pk}
        )

    def test_get_songs_for_artist(self):
        response = self.client.get(self.song_albums_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(
            response.data["data"][0]["title"], self.artist_song_album.title
        )
