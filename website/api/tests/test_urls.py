from apps.contact_groups.models import ContactGroup
from apps.message_templates.models import MessageTemplate
from apps.notifications.models import SentNotification, NotificationTemplate
from services.tests.test_settings import Settings


class TestUrls(Settings):
    def setUp(self):
        contact_group = ContactGroup.objects.create(group_name='contact_group', filename='filename')
        message_template = MessageTemplate.objects.create(name='message_template', text='123')
        notification_template = NotificationTemplate.objects.create(
            name='notification_template',
            contact_group=contact_group,
            message_template=message_template,
        )
        self.notification = SentNotification.objects.create(notification_template=notification_template)

    def test_update_url(self):
        response = self.client.post(f'/api/v1/notifications/update/{self.notification.id}/')
        self.assertEqual(response.status_code, 403)
