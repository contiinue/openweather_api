from celery import Celery
from .celery_settings import CeleryConfig

celery = Celery("worker")
celery.config_from_object(CeleryConfig, namespace="CELERY")


celery.autodiscover_tasks()

celery.conf.imports = [
    "parser.tasks",
]


celery.conf.beat_schedule = {
    "add-every-60-seconds": {
        "task": "parser.tasks.update_weather",
        "schedule": 10.0,
    },
}
