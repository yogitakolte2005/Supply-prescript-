from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SupplyPrescript API"
    app_version: str = "1.0.0"
    database_url: str = "postgresql+psycopg://postgres:password@localhost:5432/supplyprescript"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
