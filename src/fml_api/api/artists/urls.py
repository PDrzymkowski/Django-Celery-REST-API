from django.urls import path
from rest_framework.routers import DefaultRouter

from .v1.views import ArtistSongAlbumsView
from .v1.views import ArtistSongsView
from .v1.views import ArtistViewSet

router = DefaultRouter()
router.register(r"artists", ArtistViewSet)

urlpatterns = router.urls + [
    path(
        "artists/<uuid:artist_id>/songs/",
        ArtistSongsView.as_view(),
        name="artist-songs",
    ),
    path(
        "artists/<uuid:artist_id>/song-albums/",
        ArtistSongAlbumsView.as_view(),
        name="artist-song-albums",
    ),
]
