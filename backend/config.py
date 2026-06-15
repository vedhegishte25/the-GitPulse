from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    github_token: str
    database_url: str
    redis_url: str = "redis://localhost:6379"
    secret_key: str
    app_env: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()