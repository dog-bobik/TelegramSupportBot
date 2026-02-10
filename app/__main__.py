"""
Application entrypoint.
"""

from app.factory import create_app_config
from app.models.config.env import AppConfig
from app.utils.logging import setup_logging, AppLogger

logger = AppLogger(name=__name__)


def main() -> None:
    setup_logging()
    config: AppConfig = create_app_config()
    logger.info("Application configuration initialized.")


if __name__ == "__main__":
    main()
