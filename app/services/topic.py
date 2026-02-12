from typing import Optional, Any, Callable, Awaitable

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.models.config import AppConfig
from app.models.sql import TopicModel
from app.models.dto import TopicDto
from app.services.database import SQLSessionContext


class TopicService:
    """
    Application service responsible for topic lifecycle.
    """

    def __init__(
        self, session_pool: async_sessionmaker[AsyncSession], config: AppConfig
    ) -> None:
        self.session_pool = session_pool
        self.config = config

    async def get_or_create(
        self, telegram_id: int, name: str, initial_message_id: int
    ) -> TopicDto:
        """
        Retrieve existing topic or create a new one.
        """
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            existing_topic: (
                TopicDto | None
            ) = await repository.topics.get_by_telegram_id(telegram_id=telegram_id)
            if existing_topic:
                return existing_topic.dto()
            new_topic = TopicModel(
                telegram_id=telegram_id,
                name=name,
                initial_message_id=initial_message_id,
            )
            await uow.commit(new_topic)
            return new_topic.dto()

    async def _get(
        self,
        getter: Callable[[Any], Awaitable[Optional[TopicModel]]],
        key: Any,
    ) -> Optional[TopicDto]:
        topic: Optional[TopicDto] = await getter(key)
        if topic is None:
            return None
        return topic.dto()

    async def get_by_id(self, topic_id: int) -> Optional[TopicDto]:
        """
        Get user by internal ID.
        """
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            return await self._get(repository.topics.get_by_id, topic_id)

    async def get_by_telegram_id(self, telegram_id: int) -> Optional[TopicDto]:
        """
        Get user by Telegram ID.
        """
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            return await self._get(repository.topics.get_by_telegram_id, telegram_id)

    async def update(self, topic: TopicDto, **kwargs: Any) -> TopicDto:
        """
        Update topic fields.
        """
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            for key, value in kwargs.items():
                if hasattr(topic, key):
                    setattr(topic, key, value)
            await repository.topics.update(topic_id=topic.id, **topic.model_state)
            await uow.commit()
            return topic
