from app.factory import create_app_config, create_dispatcher, create_bot
from aiogram import Dispatcher, Bot
from app.models.config.env import AppConfig
from app.utils.logging import setup_logging, AppLogger
from .runners import run_polling

logger = AppLogger(name=__name__)


def main() -> None:
    """
    Initialize and start the application.
    """

    setup_logging()
    config: AppConfig = create_app_config()
    dispatcher: Dispatcher = create_dispatcher(config=config)
    bot: Bot = create_bot(config=config)
    logger.info("Application configuration initialized.")
    return run_polling(dispatcher=dispatcher, bot=bot)


if __name__ == "__main__":
    main()
