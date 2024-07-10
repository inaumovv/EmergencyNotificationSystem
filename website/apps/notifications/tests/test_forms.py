from apps.contact_groups.models import ContactGroup
from apps.message_templates.models import MessageTemplate
from apps.notifications.forms import NotificationTemplateForm
from services.tests.test_settings import Settings


class TestNotificationsForm(Settings):

    def setUp(self):
        self.contact_group = ContactGroup.objects.create(group_name='test_name', filename='111')
        self.message_template = MessageTemplate.objects.create(name='test_name', text='111')

    def test_form_save(self):
        form_data = {
            'name': 'test_name',
            'contact_group': self.contact_group.id,
            'message_template': self.message_template.id
        }
        form = NotificationTemplateForm(data=form_data)
        self.assertTrue(form.is_valid())
        notification_template = form.save(commit=False)
        self.assertEqual(notification_template.name, 'test_name')
        self.assertEqual(notification_template.contact_group, self.contact_group)
        self.assertEqual(notification_template.message_template, self.message_template)