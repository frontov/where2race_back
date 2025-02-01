# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN #python main.py

#WORKDIR /app/api

# Копирование файла конфигурации
COPY uvicorn.conf.py .

# Запуск Uvicorn
CMD ["uvicorn", "uvicorn_conf:app", "--host", "0.0.0.0", "--port", "8000"]