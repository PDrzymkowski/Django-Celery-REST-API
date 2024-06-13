from __future__ import absolute_import
from __future__ import unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FancyMusicLibrary.settings")

app = Celery("fml_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
