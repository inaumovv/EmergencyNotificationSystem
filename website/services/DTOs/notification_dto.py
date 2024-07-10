from pydantic import BaseModel

from services.DTOs.DTO import DTO


class NotificationDTO(BaseModel, DTO):
    notification_id: int
    message_text: str
    filename: int