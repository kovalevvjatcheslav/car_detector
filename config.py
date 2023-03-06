from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    IMAGE_PROCESSOR_PORT: int = Field("8080", env="IMAGE_PROCESSOR_PORT")

    POSTGRES_HOST: str = Field("localhost", env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")
    POSTGRES_DB: str = Field("car_detector", env="POSTGRES_DB")
    POSTGRES_USER: str = Field("user", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("very_strong_password", env="POSTGRES_PASSWORD")


settings = Settings()
