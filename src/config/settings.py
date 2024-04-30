from pydantic_settings import BaseSettings, SettingsConfigDict


class MainSettings(BaseSettings):
    sqlalchemy_database_uri: str
    sql_host: str
    sql_port: int
    debug: int
    database: str
    google_drive_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__"
    )


settings = MainSettings()
