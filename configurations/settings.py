from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str = "postgresql+asyncpg://postgres:Sanan4ik008@127.0.0.1:5432"
    db_name: str = "mydb"
    db_test_name: str = "mydb"
    max_connection_count: int = 10

    @property
    def database_url(self) -> str:
        return f"{self.db_host}/{self.db_name}"

    @property
    def database_test_url(self) -> str:
        return f"{self.db_host}/{self.db_test_name}"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
