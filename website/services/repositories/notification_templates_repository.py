from apps.notifications.models import NotificationTemplate
from services.repositories.base_repository import BaseRepository


class NotificationTemplatesRepository(BaseRepository):
    model: NotificationTemplate = NotificationTemplate

    @classmethod
    def get_notification_templates_with_relations(
            cls,
            select_related: tuple | list,
            fields: tuple | list = None,
            **filters
    ):
        return cls.get_objects_with_relations(
            object_=cls.model.objects,
            select_related=select_related,
            fields=fields,
            **filters
        )
