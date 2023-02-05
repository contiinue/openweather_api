from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    OPEN_WEATHER_API_KEY: str

    POSTGRES_DATABASE: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    REDIS_HOST: str
    REDIS_PORT: str

    class Config:
        env_file = BASE_DIR.parent.joinpath(".env.dev")
        env_file_encoding = "utf-8"


settings = Settings()

TIME_ZONE = "Europe/Moscow"
