

uvicorn main:app --reload & celery -A worker.celery_app:celery worker & celery -A worker.celery_app:celery beat

