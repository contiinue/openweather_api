from celery import Celery, current_app

from config import settings

CELERY_BROKER_URL = (
    CELERY_RESULT_BACKEND
) = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"

celery = Celery("worker", broker=CELERY_BROKER_URL)
celery.config_from_object("worker.celery_settings", namespace="S3")


celery.autodiscover_tasks()


tasks = current_app.tasks.keys()

celery.conf.imports = [
    "parser.tasks",
]


celery.conf.beat_schedule = {
    "add-every-60-seconds": {
        "task": "parser.tasks.update_weather",
        "schedule": 60.0,
    },
}
