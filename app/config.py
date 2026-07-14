from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application Settings
    Loaded automatically from .env
    """

    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    DATABASE_URL: str

    LLM_PROVIDER: str
    GOOGLE_API_KEY: str = ""

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()