from operator import index

from fastapi import FastAPI, BackgroundTasks
from tasks import long_running_task
from pydantic import BaseModel

app = FastAPI()


class TaskRequest(BaseModel):
	duration: int


@app.get("/")
async def read_root():
	return {"message": "Hello World"}


@app.get("/health")
async def health():
	return {"status": "ok"}


@app.post("/run-task/")
async def run_task(request: TaskRequest):
	# Enqueue the Celery task
	result = long_running_task.delay(request.duration)

	# Return the task ID immediately
	return {"task_id": result.id, "state": result.state}


@app.get("/get-task/{task_id}")
async def task_status(task_id: str):
	# Check the status of the task
	result = long_running_task.AsyncResult(task_id)
	return {"task_id": task_id, "state": result.state, "result": result.result}
