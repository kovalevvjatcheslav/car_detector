from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    IMAGE_PROCESSOR_PORT: int = Field(8080, env="IMAGE_PROCESSOR_PORT")

    DETECTOR_HOST: str = Field("detector", env="DETECTOR_HOST")
    DETECTOR_PORT: int = Field(8081, env="DETECTOR_PORT")

    POSTGRES_HOST: str = Field("localhost", env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")
    POSTGRES_DB: str = Field("car_detector", env="POSTGRES_DB")
    POSTGRES_USER: str = Field("user", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("very_strong_password", env="POSTGRES_PASSWORD")
    POSTGRES_TEST_DB: str = Field("test_db", env="POSTGRES_TEST_DB")

    IS_TEST: bool = Field(False, env="IS_TEST")

    LOG_LEVEL: str = Field("debug", env="LOGLEVEL")


settings = Settings()
