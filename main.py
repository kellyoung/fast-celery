from celery import Celery
from project import create_app

app = create_app()
celery = app.celery_app

celery = Celery(
    "fast-celery",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)
