from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    API_SERVICE: int = Field("8080", env="API_SERVICE")

    POSTGRES_HOST: str = Field("localhost", env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")
    POSTGRES_DB: str = Field("car_detector", env="POSTGRES_DB")
    POSTGRES_USER: str = Field("user", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("very_strong_password", env="POSTGRES_PASSWORD")


settings = Settings()
