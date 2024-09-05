import time


def background_task(duration):
	"""Function that simulates a long-running task."""
	print(f"Processing task for {duration} seconds...")
	time.sleep(duration)
	return f"Task completed after {duration} seconds."
