from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings powered by Pydantic Settings.
    Reads environment variables and optional .env file.
    """
    PROJECT_NAME: str = "AI-Powered Student Learning System"
    API_V1_STR: str = "/api/v1"

    # Database settings
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/learning_system"

    # Firebase Authentication settings
    FIREBASE_CREDENTIALS: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
