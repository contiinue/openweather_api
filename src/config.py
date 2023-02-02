from pydantic import BaseSettings


class Settings(BaseSettings):
    OPEN_WEATHER_API_KEY: str

    POSTGRES_DATABASE: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
