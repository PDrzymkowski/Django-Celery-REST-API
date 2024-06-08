from rest_framework import viewsets

from fml_api.api.pagination import SmallPagesPagination
from fml_api.api.serializers.music_genre import MusicGenreSerializer
from fml_api.models import MusicGenre


class MusicGenreViewSet(viewsets.ModelViewSet):
    """ViewSet for MusicGenre model."""

    queryset = MusicGenre.objects.all()
    serializer_class = MusicGenreSerializer
    pagination_class = SmallPagesPagination
