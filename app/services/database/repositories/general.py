from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession


class Repository:
    """
    Base repository abstraction.
    Provides access to SQLAlchemt session.
    """

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session)
