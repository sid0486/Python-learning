from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "phase-0-foundation"
    debug: bool = False
    database_url: str
    secret_key: str

    # add these 3 — they exist in your .env for PostgreSQL
    postgres_user: str
    postgres_password: str
    postgres_db: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"      # ← ignores any extra vars in .env
    )

settings = Settings()