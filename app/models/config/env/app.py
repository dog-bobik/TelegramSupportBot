"""
Application configuration aggregator.
"""

from pydantic import BaseModel


class AppConfig(BaseModel):
    """Aggregates all application env configs."""

    # TODO : Will include TG, DB, Common configs later
    pass
