from apps.contact_groups.models import ContactGroup
from apps.message_templates.models import MessageTemplate
from apps.notifications.models import NotificationTemplate, SentNotification
from services.tests.test_settings import Settings


class TestNotificationsViews(Settings):
    def setUp(self):
        super().setUp()
        self.contact_group = ContactGroup.objects.create(group_name='test_group_name', filename='test')
        self.message_template = MessageTemplate.objects.create(name='test_message_name', text='test_message_text')
        self.notification_template = NotificationTemplate.objects.create(
            name='test_notification_name',
            contact_group=self.contact_group,
            message_template=self.message_template
        )

    def test_add_view(self):
        form_data = {
            'name': 'Test Name',
            'contact_group': self.contact_group.id,
            'message_template': self.message_template.id
        }
        response = self.authorized_client.post('/add/', data=form_data)
        self.assertRedirects(response, '/')
        contact_group = NotificationTemplate.objects.filter(name='Test Name')
        self.assertTrue(contact_group.exists())

    def test_edit_view(self):
        form_data = {
            'name': 'updated name',
            'contact_group': self.contact_group.id,
            'message_template': self.message_template.id
        }
        response = self.authorized_client.post(f'/edit/{self.notification_template.id}/', data=form_data)
        self.assertRedirects(response, '/')
        self.assertTrue(NotificationTemplate.objects.filter(name='updated name').exists())

    def test_delete_view(self):
        response = self.authorized_client.post(f'/delete/{self.notification_template.id}/')
        self.assertRedirects(response, '/')
        self.assertFalse(ContactGroup.objects.filter(group_name='updated name').exists())

    def test_send_notification_view(self):
        data = {
            'notification_template_id': self.notification_template.id
        }
        response = self.authorized_client.get('/send/', data=data)
        self.assertRedirects(response, '/sent-notifications/')
        self.assertTrue(SentNotification.objects.exists())
