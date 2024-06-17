import os
import shutil
import zipfile

import pendulum
from celery import shared_task
from django.conf import settings

from common.utils import queryset_to_csv
from fml_api.models import Artist
from fml_api.models import MusicGenre
from fml_api.models import Song
from fml_api.models import SongAlbum


__all__ = ["dump_data_to_csv"]


@shared_task
def dump_data_to_csv():
    """Dumps data from the models to CSV files and packs them into a ZIP file."""
    # Create a timestamped directory for the CSV files
    timestamp = pendulum.now().strftime("%Y%m%d%H%M%S")
    directory = os.path.join(settings.MEDIA_ROOT, f"data_dumps/{timestamp}")
    csv_dir = os.path.join(directory, f"csv")
    os.makedirs(csv_dir, exist_ok=True)

    # Dump data from each model to a CSV file
    queryset_to_csv(Artist.objects.all(), os.path.join(csv_dir, "artists.csv"))
    queryset_to_csv(MusicGenre.objects.all(), os.path.join(csv_dir, "genres.csv"))
    queryset_to_csv(Song.objects.all(), os.path.join(csv_dir, "songs.csv"))
    queryset_to_csv(SongAlbum.objects.all(), os.path.join(csv_dir, "albums.csv"))

    # Create a ZIP file containing all the CSV files
    zip_file_path = os.path.join(directory, f"data_dumps_{timestamp}.zip")
    with zipfile.ZipFile(zip_file_path, "w") as zipf:
        for root, _, files in os.walk(csv_dir):
            for file in files:
                zipf.write(
                    os.path.join(root, file),
                    os.path.relpath(os.path.join(root, file), directory),
                )

    # delete the directory with CSV files
    shutil.rmtree(csv_dir)
    return zip_file_path
