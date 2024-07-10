from apps.message_templates.models import MessageTemplate
from services.tests.test_settings import Settings


class TestMessageTemplatesViews(Settings):

    def setUp(self):
        super().setUp()
        self.message_template = MessageTemplate.objects.create(name='test_name_', text='test_text_')

    def test_edit_view(self):
        data = {
            'name': 'test_name_1',
            'text': 'test_text_1'
        }

        response = self.authorized_client.post(f'/message-templates/edit/{self.message_template.id}/', data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertTrue(MessageTemplate.objects.filter(name='test_name_1').exists())

    def test_delete_view(self):
        count_before = MessageTemplate.objects.count()

        response = self.authorized_client.post(f'/message-templates/delete/{self.message_template.id}/', follow=True)
        self.assertRedirects(response, '/message-templates/')

        count_after = MessageTemplate.objects.count()
        self.assertFalse(count_after == count_before)





