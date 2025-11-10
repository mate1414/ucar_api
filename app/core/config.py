from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "dev"

    APP_NAME: str = "ucar"
    APP_DESCRIPTION: str = "Ucar API"

    # Database
    SQLALCHEMY_DATABASE_URL: str = "postgres://docker:docker@localhost:5432/ucar"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
