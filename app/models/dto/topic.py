from app.models import PydanticModel


class TopicDto(PydanticModel):
    """
    Topic domain data.
    """

    id: int
    telegram_id: int

    initial_message_id: int

    name: str
    is_translating_enabled: bool
