from rest_framework import viewsets

from fml_api.api.pagination import SmallPagesPagination
from fml_api.api.serializers.song_album import SongAlbumSerializer
from fml_api.models import SongAlbum


class SongAlbumViewSet(viewsets.ModelViewSet):
    """ViewSet for SongAlbum model."""

    queryset = SongAlbum.objects.all()
    serializer_class = SongAlbumSerializer
    pagination_class = SmallPagesPagination
