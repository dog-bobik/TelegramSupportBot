from __future__ import annotations
from aiogram import Bot, Dispatcher

from app.models.config import AppConfig


async def polling_startup(bots: list[Bot], config: AppConfig) -> None:
    """
    Clean webhook before starting polling mode.
    """

    for bot in bots:
        await bot.delete_webhook(
            drop_pending_updates=config.telegram.drop_pending_updates
        )


def run_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    """
    Configure and launch bot in polling mode.
    """

    dispatcher.startup.register(polling_startup)
    return dispatcher.run_polling(bot)
