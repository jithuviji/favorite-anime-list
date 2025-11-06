from celery import Celery
import time

# Create Celery app instance
app = Celery(
    'tasks',  # this must match the filename
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@app.task(name='tasks.power_up')  # 👈 explicit task name helps avoid registration issues
def power_up(name):
    time.sleep(5)
    return f"{name.upper()} is powered up!"
