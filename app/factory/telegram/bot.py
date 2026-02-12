from __future__ import annotations

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from app.models.config import AppConfig


def create_bot(config: AppConfig) -> Bot:
    """
    Create and return Telegram Bot instance.
    """
    session: AiohttpSession = AiohttpSession(timeout=30)
    return Bot(
        token=config.telegram.bot_token,
        session=session,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            link_preview_is_disabled=True,
        ),
    )
