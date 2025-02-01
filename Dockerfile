# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .
COPY /etc/letsencrypt/live/back.where2race.ru/fullchain.pem ./api/
COPY /etc/letsencrypt/live/back.where2race.ru/privkey.pem ./api/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN python main.py

WORKDIR /app/api


# Expose the port that Uvicorn will run on
EXPOSE 443

# Command to run the application using Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile", "privkey.pem", "--ssl-certfile", "fullchain.pem"]

