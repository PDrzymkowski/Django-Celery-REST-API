# myapp/management/commands/dump_to_csv.py
from django.core.management.base import BaseCommand

from common.tasks.dump_data_to_csv import dump_data_to_csv


class Command(BaseCommand):
    help = "Runs a task to dump data to CSV"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting data dump to CSV..."))
        dump_data_to_csv()
        self.stdout.write(
            self.style.SUCCESS("Data dump to CSV has been initiated successfully")
        )
