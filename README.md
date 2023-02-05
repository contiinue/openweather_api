g# Тестовое задание
___

### Запуск

## Установка

```shell
git clone git@github.com:contiinue/openweather_api.git &
cd openweather_api/
```

### Необходимо создать в корневой папке .env файл или использовать комманду

```shell
mv .env.example .env
```

### Необходимые переменные, если создавать вручную.
```dotenv
OPEN_WEATHER_API_KEY=439d4b804bc8187953eb36d2a8c26a02  # рабочий 

# Postgres
POSTGRES_DATABASE='postgres'
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
docker-compose up -d --build
```