from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include(f"fml_api.api.artists.urls")),
    path("", include(f"fml_api.api.song_albums.urls")),
    path("", include(f"fml_api.api.music_genres.urls")),
    path("", include(f"fml_api.api.songs.urls")),
    path("admin/", include(f"fml_api.api.admin.urls")),
]
