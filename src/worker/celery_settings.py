from config import BASE_DIR, TIME_ZONE, settings

# Celery
CELERY_broker_url = (
    result_backend
) = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"
timezone = TIME_ZONE
CELERY_broker_transport_options = {"visibility_timeout": 3600}
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
accept_content = ["application/json"]
task_serializer = "json"
result_serializer = "json"
s3_base_path = BASE_DIR
