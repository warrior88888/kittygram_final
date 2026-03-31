from pydantic_settings import BaseSettings, SettingsConfigDict

from .django import DjangoConfig
from .postgres import PostgresConfig


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_prefix="KT__",
        env_nested_delimiter="__",
    )

    django: DjangoConfig
    postgres: PostgresConfig


app_config = Settings() # type: ignore[reportCallIssue]
