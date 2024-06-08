from rest_framework import serializers

from fml_api.models import Song

__all__ = ["SongSerializer"]


class SongSerializer(serializers.ModelSerializer):
    """Serializer for Song model."""

    class Meta:
        model = Song
        fields = "__all__"
