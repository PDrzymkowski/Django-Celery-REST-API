from rest_framework import generics
from rest_framework import viewsets

from fml_api.api.pagination import SmallPagesPagination
from fml_api.api.serializers.artist import ArtistSerializer
from fml_api.api.serializers.song import SongSerializer
from fml_api.api.serializers.song_album import SongAlbumSerializer
from fml_api.models import Artist
from fml_api.models import Song
from fml_api.models import SongAlbum


class ArtistViewSet(viewsets.ModelViewSet):
    """ViewSet for Artist model."""

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = SmallPagesPagination


class ArtistSongsView(generics.ListAPIView):
    """View for Songs released by a particular Artist."""

    serializer_class = SongSerializer

    def get_queryset(self):
        artist_id = self.kwargs["artist_id"]
        return Song.objects.filter(artist_id=artist_id)


class ArtistSongAlbumsView(generics.ListAPIView):
    """View for Song Albums released by a particular Artist."""

    serializer_class = SongAlbumSerializer

    def get_queryset(self):
        artist_id = self.kwargs["artist_id"]
        return SongAlbum.objects.filter(artist_id=artist_id)
