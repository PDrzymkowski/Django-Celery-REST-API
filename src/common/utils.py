import csv

from django.db.models import QuerySet


def queryset_to_csv(queryset: QuerySet, file_name: str):
    """Helper function to dump a Django queryset to a CSV file."""
    model = queryset.model
    field_names = [field.name for field in model._meta.fields]

    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
