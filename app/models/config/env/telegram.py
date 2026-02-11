from .base import EnvSettings


class TelegramConfig(EnvSettings, env_prefix="TELEGRAM_"):
    """
    Telegram-related environment variables.
    Contains all configuration required to initialize
    the telegram bot and dispatcher.
    """

    bot_token: str
    locales: list[str] = ["ru"]
    drop_pending_updates: bool = False
