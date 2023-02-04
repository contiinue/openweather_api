# Тестовое задание
___

### Запуск

## Установка с докером

### Необходимо создать .env файл,
```
OPEN_WEATHER_API_KEY=439d4b804bc8187953eb36d2a8c26a02  # рабочий 

# Postgres
POSTGRES_DATABASE='parserwithsсrapy'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='2407'
POSTGRES_HOST='db'
POSTGRES_PORT='5432'

# Redis
REDIS_HOST='redis'
REDIS_PORT='6379'

```

## Запуск
```
docker-compose up --build
```