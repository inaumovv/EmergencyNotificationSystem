from apps.notifications.models import SentNotification
from services.repositories.base_repository import BaseRepository


class SentNotificationsRepository(BaseRepository):
    model: SentNotification = SentNotification

    @classmethod
    def get_sent_notifications(cls, fields: tuple | list = None, **filters):
        return cls.get_objects(object_=cls.model.objects, fields=fields, **filters)

    @classmethod
    def get_sent_notifications_with_relations(cls, select_related: tuple | list, fields: tuple | list = None, **filters):
        return cls.get_objects_with_relations(
            object_=cls.model.objects,
            select_related=select_related,
            fields=fields,
            **filters
        )

    @classmethod
    def create_sent_notification(cls, notification_template_id: int):
        return cls.create_object(object_=cls.model.objects, notification_template_id=notification_template_id)
