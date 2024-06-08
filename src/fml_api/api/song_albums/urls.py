from rest_framework.routers import DefaultRouter

from .v1.views import SongAlbumViewSet

router = DefaultRouter()
router.register(r"song-albums", SongAlbumViewSet)

urlpatterns = router.urls
