# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY python-gmqtt-sub-log.py /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir gmqtt

# Make port 1883 available to the world outside this container
EXPOSE 1883


# Run mqtt_client.py when the container launches
CMD ["python", "python-gmqtt-sub-log.py"]