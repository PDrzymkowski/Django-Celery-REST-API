import uuid

from django.db import models

# Create your models here.


class BaseModel(models.Model):
    """
    An abstract base class model that provides UUID id and self-updating `created_at` and `updated_at` fields.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MusicGenre(BaseModel):
    """Model representing a music genre."""

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Artist(BaseModel):
    """Model representing an artist."""

    name = models.CharField(max_length=256)
    bio = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def genres(self) -> list["MusicGenre"]:
        return [
            genre for genre in self.song_set.values_list("genre", flat=True).distinct()
        ]


class Song(BaseModel):
    """Model representing a song."""

    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(MusicGenre, on_delete=models.SET_NULL, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    length = models.DurationField(help_text="Duration of the song")

    def __str__(self):
        return f"'{self.title}' by {self.artist.name}"


class SongAlbum(BaseModel):
    """Model representing a song album."""

    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    genre = models.ForeignKey(MusicGenre, on_delete=models.SET_NULL, null=True)
    songs = models.ManyToManyField(Song, related_name="albums")

    def __str__(self):
        return f"'{self.title}' by {self.artist.name}"
