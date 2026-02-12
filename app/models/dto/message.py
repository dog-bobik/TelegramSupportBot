from typing import Optional
from app.models import PydanticModel


class MessageDto(PydanticModel):
    """
    Message domain data.
    """

    id: int
    telegram_id: int
    chat_id: int

    from_user_id: int

    original_message_id: int  # Sended by AiogramUser
    forwarded_message_id: int  # Sended by AiogramBot

    text: Optional[str] = None
