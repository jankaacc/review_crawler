import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawler.settings")

celery_app = Celery("crawler")
celery_app.config_from_object(settings, namespace="CELERY")
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule["fetch-reviews"] = {
    "task": "gp_crawler.tasks.fetch_reviews",
    "schedule": crontab(minute=0, hour="*"),
    "kwargs": {"pages": 3, "page_size": 3},
}
