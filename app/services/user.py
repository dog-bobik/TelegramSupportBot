from typing import Optional, Any, Callable, Awaitable

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.models.config import AppConfig
from app.models.sql import UserModel
from app.models.dto import UserDto
from app.services.database import SQLSessionContext


class UserService:
    """
    Application service responsible for user lifecycle.
    """

    def __init__(
        self, session_pool: async_sessionmaker[AsyncSession], config: AppConfig
    ) -> None:
        self.session_pool = session_pool
        self.config = config

    async def get_or_create(
        self,
        telegram_id: int,
        username: str,
        locale: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
    ) -> UserDto:
        """
        Retrieve existing user or create a new one.
        """
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            existing_user = await repository.users.get_by_telegram_id(
                telegram_id=telegram_id
            )
            if existing_user:
                return existing_user.dto()

            new_user = UserModel(
                telegram_id=telegram_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                locale=locale,
            )
            await uow.commit(new_user)
            return new_user.dto()

    async def _get(
        self,
        getter: Callable[[Any], Awaitable[Optional[UserModel]]],
        key: Any,
    ) -> Optional[UserDto]:
        user: Optional[UserModel] = await getter(key)
        if user is None:
            return None
        return user.dto()

    async def get_by_id(self, user_id: int) -> Optional[UserDto]:
        """
        Get user by internal ID.
        """
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            return await self._get(repository.users.get_by_id, user_id)

    async def get_by_telegram_id(self, telegram_id: int) -> Optional[UserDto]:
        """
        Get user by Telegram ID.
        """
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            return await self._get(repository.users.get_by_telegram_id, telegram_id)

    async def update(self, user: UserDto, **kwargs: Any) -> UserDto:
        """
        Update user fields.
        """
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            await repository.users.update(user_id=user.id, **user.model_state)
            await uow.commit()
            return user
