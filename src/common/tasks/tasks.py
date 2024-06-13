from celery import shared_task


@shared_task
def debug_task(self):
    print(f"Hello")
