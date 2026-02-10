"""
Application entrypoint.
"""

from app.factory import create_app_config
from app.models.config.env import AppConfig


def main() -> None:
    config: AppConfig = create_app_config()
    print("Application configuration initialized")


if __name__ == "__main__":
    main()
