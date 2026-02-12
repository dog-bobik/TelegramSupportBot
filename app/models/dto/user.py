from typing import Optional
from app.models import PydanticModel


class UserDto(PydanticModel):
    """
    User domain data.
    """

    id: int
    telegram_id: int

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None

    locale: str
    is_blocked: bool
    is_bot_blocked: bool
