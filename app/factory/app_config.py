"""
Application configuration factory.
"""

from __future__ import annotations
from app.models.config.env import (
    AppConfig,
    PostgresConfig,
    SQLAlchemyConfig,
    TelegramConfig,
)


def create_app_config() -> AppConfig:
    """Create application configuration."""
    return AppConfig(
        telegram=TelegramConfig(),
        postgres=PostgresConfig(),
        sql_alchemy=SQLAlchemyConfig(),
    )
