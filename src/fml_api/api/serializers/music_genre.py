from rest_framework import serializers

from fml_api.models import MusicGenre

__all__ = ["MusicGenreSerializer"]


class MusicGenreSerializer(serializers.ModelSerializer):
    """Serializer for MusicGenre model."""

    class Meta:
        model = MusicGenre
        fields = "__all__"
