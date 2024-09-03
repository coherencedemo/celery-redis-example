from celery import Celery
import time

# Initialize Celery with Redis as the broker
app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


# Define a long-running task
@app.task
def long_running_task(duration):
	print(f"Task started, will run for {duration} seconds...")
	time.sleep(duration)  # Simulate a long-running job
	return f"Task completed after {duration} seconds."
