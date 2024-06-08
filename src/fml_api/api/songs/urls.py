from rest_framework.routers import DefaultRouter

from .v1.views import SongViewSet

router = DefaultRouter()
router.register(r"songs", SongViewSet)

urlpatterns = router.urls
