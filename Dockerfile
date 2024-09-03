# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Celery worker
CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]

# Define the command to run the fastapi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]