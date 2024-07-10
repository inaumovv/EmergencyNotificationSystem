import json
import os

from rest_framework.test import APIClient

from apps.contact_groups.models import ContactGroup
from apps.message_templates.models import MessageTemplate
from apps.notifications.models import NotificationTemplate, SentNotification
from services.tests.test_settings import Settings

from dotenv import load_dotenv

load_dotenv()


class TestViews(Settings):
    api_token = os.getenv('API_TOKEN')

    def setUp(self):
        contact_group = ContactGroup.objects.create(group_name='contact_group_', filename='filename')
        message_template = MessageTemplate.objects.create(name='message_template_', text='123')
        notification_template = NotificationTemplate.objects.create(
            name='notification_template_',
            contact_group=contact_group,
            message_template=message_template,
        )
        self.notification = SentNotification.objects.create(notification_template=notification_template)

    def test_update_api_view(self):
        data = {
            'status': 'в обработке',
            'delivery_time': '2024-07-08 20:39:22'
        }
        response = APIClient().put(
            headers={'Authorization': f'Token {self.api_token}'},
            path=f'/api/v1/notifications/update/{self.notification.id}/',
            data=json.dumps(data),
            format='json'
        )
        self.assertEqual(response.status_code, 200)

        sent_notification = SentNotification.objects.get(id=self.notification.id)

        self.assertTrue(
            sent_notification.status == data['status'] and sent_notification.delivery_time == data['delivery_time']
        )
