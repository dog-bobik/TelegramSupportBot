"""
Base configuration schema.
Defines common behavior for environment-based
configd.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from app.const import ENV_FILE


class EnvSettings(BaseSettings):
    """
    Base class for all env-backend config
    models.
    """

    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
    )
