
# Используем официальный образ Python
FROM python:3.9

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python main.py

WORKDIR /app/api

# Копируем код приложения
COPY . .

# Указываем команду для запуска приложения
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "/etc/letsencrypt/live/api.where2race.ru/privkey.pem", "--ssl-certfile", "/etc/letsencrypt/live/api.where2race.ru/fullchain.pem"]
