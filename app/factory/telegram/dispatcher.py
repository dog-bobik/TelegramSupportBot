from __future__ import annotations

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.factory import create_session_pool
from app.models.config import AppConfig
from app.services import UserService, TopicService
from .i18n import setup_i18n_middleware


def create_dispatcher(config: AppConfig) -> Dispatcher:
    """
    Create Dispatcher with in-memory FSM storage.
    """

    session_pool: async_sessionmaker[AsyncSession] = create_session_pool(config=config)
    dispatcher: Dispatcher = Dispatcher(
        name="main_dispatcher",
        storage=MemoryStorage(),
        config=config,
        session_pool=session_pool,
        user_service=UserService(session_pool=session_pool, config=config),
        topic_service=TopicService(session_pool=session_pool, config=config),
    )

    setup_i18n_middleware()  # Stub
    # TODO : will include routers and middlewares
    return dispatcher
