from rest_framework import viewsets

from fml_api.api.pagination import SmallPagesPagination
from fml_api.api.serializers.song import SongSerializer
from fml_api.models import Song


class SongViewSet(viewsets.ModelViewSet):
    """ViewSet for Song model."""

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = SmallPagesPagination
