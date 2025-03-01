# Use an official Python runtime as base image
FROM python:3.9

# Copy the project files into the container
ADD main.py main.py

# Command to run the application
CMD ["python", "main.py"]
