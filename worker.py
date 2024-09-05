import os
from rq import Worker, Queue
from redis import Redis

# Environment variables for Redis configuration
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_conn = Redis(host=redis_host, port=6379)

# List of queues to which this worker should listen
queues = os.getenv('QUEUES', 'default').split(',')

# Start the worker with the specified queues
worker = Worker(queues=queues, connection=redis_conn)
worker.work()
