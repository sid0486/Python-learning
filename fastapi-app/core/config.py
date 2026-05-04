from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "phase-0-foundation"
    debug: bool = False
    database_url: str
    secret_key: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()