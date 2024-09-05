from fastapi import FastAPI
from rq import Queue
from redis import Redis
from rq.job import Job

app = FastAPI()

# Establish connection to Redis
redis_host = "redis"  # This will be your container name for Redis in Docker
redis_conn = Redis(host=redis_host, port=6379)
queue = Queue(connection=redis_conn)

@app.post("/tasks/")
def enqueue_task(duration: int):
    """Endpoint to receive duration and enqueue a task."""
    job = queue.enqueue('tasks.background_task', duration)
    return {"job_id": job.id, "status": "Task enqueued"}

@app.get("/tasks/{job_id}")
def get_task_status(job_id: str):
    """Endpoint to check the status of a task."""
    job = Job.fetch(job_id, connection=redis_conn)
    return {"job_id": job_id, "status": job.get_status(), "result": job.result}
