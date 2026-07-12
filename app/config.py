from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    # -----------------------------
    # Application
    # -----------------------------
    APP_NAME: str = "Stay Fresh AI Backend"
    APP_ENV: str = "development"
    DEBUG: bool = True

    # -----------------------------
    # Gemini
    # -----------------------------
    GOOGLE_API_KEY: str

    # -----------------------------
    # Database
    # -----------------------------
    DATABASE_URL: str = "sqlite:///./stayfresh.db"

    # -----------------------------
    # VasyERP
    # -----------------------------
    VASYERP_URL: str
    VASYERP_USERNAME: str
    VASYERP_PASSWORD: str

    # -----------------------------
    # Uploads
    # -----------------------------
    UPLOAD_DIR: str = "uploads"

    # -----------------------------
    # Logs
    # -----------------------------
    LOG_DIR: str = "logs"
    GOOGLE_SHEET_NAME: str
    GOOGLE_CREDENTIALS: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()


# Create required folders automatically
Path(settings.UPLOAD_DIR).mkdir(exist_ok=True)
Path(settings.LOG_DIR).mkdir(exist_ok=True)