from rest_framework import serializers

from fml_api.models import Artist

__all__ = ["ArtistSerializer"]


class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artist model."""

    class Meta:
        model = Artist
        fields = "__all__"
