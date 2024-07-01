from apps.notifications.models import SentNotification
from services.repositories.base_repository import BaseRepository


class SentNotificationsRepository(BaseRepository):
    model: SentNotification = SentNotification

    @classmethod
    def get_sent_notifications(cls, fields: tuple | list = None):
        return cls.get_objects(object_=cls.model.objects, fields=fields)

    @classmethod
    def create_sent_notification(cls, notification_template_id: int):
        return cls.create_object(object_=cls.model.objects, notification_template_id=notification_template_id)
