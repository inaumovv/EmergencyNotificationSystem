from apps.message_templates.models import MessageTemplate
from services.repositories.base_repository import BaseRepository


class MessageTemplatesRepository(BaseRepository):
    model: MessageTemplate = MessageTemplate

    @classmethod
    def get_all_message_templates(cls, fields: list | tuple = None, **filters):
        return cls.get_objects(object_=cls.model.objects, fields=fields, **filters)
