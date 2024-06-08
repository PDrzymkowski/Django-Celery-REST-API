from rest_framework.routers import DefaultRouter

from .v1.views import MusicGenreViewSet

router = DefaultRouter()
router.register(r"music-genres", MusicGenreViewSet)

urlpatterns = router.urls
