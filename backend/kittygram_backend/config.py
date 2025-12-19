from pydantic import Field
from pydantic.types import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


class DatabaseConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="DB_")

    HOST: SecretStr
    PORT: int
    USER: str
    PASS: SecretStr
    NAME: str


class DjangoConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="DJANGO_")

    DEBUG: bool
    SECRET_KEY: SecretStr


class ServerConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="SERVER_")

    IP: str
    DOMAIN: str

    @property
    def allowed_hosts(self):
        return [self.IP, self.DOMAIN, '127.0.0.1', 'localhost']


class Config(ConfigBase):
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)
    django: DjangoConfig = Field(default_factory=DjangoConfig)
    server: ServerConfig = Field(default_factory=ServerConfig)


settings = Config()
