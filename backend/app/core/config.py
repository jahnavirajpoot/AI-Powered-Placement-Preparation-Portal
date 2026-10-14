from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[3]
class Settings(BaseSettings):
    app_name: str = "AP3"
    app_env: str = "development"
    debug: bool = True

    database_url: str

    redis_url: str

    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str
    minio_bucket: str
    minio_secure: bool = False

    jwt_secret_key: str
    jwt_access_token_expire_minutes: int = 15
    jwt_refresh_token_expire_days: int = 7

    llm_provider: str = "ollama"
    ollama_base_url: str = "http://ollama:11434"

    openai_api_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()