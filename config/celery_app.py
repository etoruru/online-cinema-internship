import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("online_cinema")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.update(
    task_queues={
        "video": {
            "exchange": "video",
            "routing_key": "video",
        },
        "upload": {
            "exchange": "upload",
            "routing_key": "upload",
        },
    },
    task_routes={
        "online_cinema.encoder.tasks.convert_video_to_hls": {
            "queue": "video",
            "routing_key": "online_cinema.encoder.tasks.convert_video_to_hls",
        },
        "online_cinema.encoder.file_uploader.file_upload": {
            "queue": "upload",
            "routing_key": "online_cinema.encoder.file_uploader.file_upload",
        },
    },
)
