from worker.celery_app import celery

from .weather_spider import start_spider


@celery.task()
def update_weather():
    start_spider()
