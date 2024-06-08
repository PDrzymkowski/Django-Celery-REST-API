from rest_framework import serializers

from fml_api.models import SongAlbum

__all__ = ["SongAlbumSerializer"]


class SongAlbumSerializer(serializers.ModelSerializer):
    """Serializer for SongAlbum model."""

    class Meta:
        model = SongAlbum
        fields = "__all__"
