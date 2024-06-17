from django.urls import path
from rest_framework.routers import DefaultRouter

from .v1.views import DataDumpAPI

router = DefaultRouter()

urlpatterns = router.urls + [
    path("dump-data", DataDumpAPI.as_view(), name="dump-data"),
]
