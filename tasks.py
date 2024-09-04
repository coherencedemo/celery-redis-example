import os
from celery import Celery
import time

# Initialize Celery with Redis as the broker
REDIS_URL = os.getenv("REDIS_QUEUE_URL", "redis://queue:6379/0")

app = Celery('tasks', broker='redis://redis_queue:6379/0', backend='redis://redis_queue:6379/0')


# Define a long-running task
@app.task
def long_running_task(duration):
	print(f"Task started, will run for {duration} seconds...")
	time.sleep(duration)  # Simulate a long-running job
	return f"Task completed after {duration} seconds."
