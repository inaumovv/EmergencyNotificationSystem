from django import template

from services.repositories.notification_templates_repository import NotificationTemplatesRepository
from services.repositories.sent_notifications_repository import SentNotificationsRepository

register = template.Library()


@register.simple_tag
def get_notification_templates():
    return NotificationTemplatesRepository.get_notification_templates_with_relations(
        select_related=('contact_group', 'message_template'),
        fields=(
            'contact_group',
            'message_template',
            'contact_group__group_name',
            'message_template__name',
            'id',
            'name',
        )
    )


@register.simple_tag
def get_sent_notifications():
    return SentNotificationsRepository.get_sent_notifications(
        fields=('id', 'status', 'created_at', 'delivery_time')
    )
