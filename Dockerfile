# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5005

# Set any necessary environment variables
ENV FLASK_APP=app.py

# Run the command to start the app
CMD ["flask", "run", "--host=0.0.0.0"]
