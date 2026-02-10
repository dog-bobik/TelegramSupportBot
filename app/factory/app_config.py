"""
Application configuration factory.
"""

from __future__ import annotations
from app.models.config.env import AppConfig


def create_app_config() -> AppConfig:
    """Create application configuration."""
    return AppConfig()
