from celery import Celery

# Create Celery app and connect it to Redis
celery_app = Celery(
    "power_up_app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# Optional: display tasks in console
celery_app.conf.task_track_started = True
