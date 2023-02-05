sleep 10

cd app/

alembic upgrade 4e6afe947aed

cd src/
uvicorn main:app --host 0.0.0.0 --port 8000 & celery -A worker.celery_app:celery worker & celery -A worker.celery_app:celery beat

