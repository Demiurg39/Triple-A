import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "triple_a.settings")
app = Celery("triple_a")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
