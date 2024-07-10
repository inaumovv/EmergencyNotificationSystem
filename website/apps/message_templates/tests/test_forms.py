from services.tests.test_settings import Settings
from ..models import MessageTemplate


class TestMessageTemplatesForms(Settings):

    def test_valid_form(self):
        count_before = MessageTemplate.objects.count()

        form_data = {
            'name': '1',
            'text': 1
        }

        response = self.authorized_client.post('/message-templates/add/', data=form_data)
        self.assertRedirects(response, '/message-templates/')
        count_after = MessageTemplate.objects.count()
        self.assertFalse(count_before == count_after)

    def test_invalid_form(self):
        count_before = MessageTemplate.objects.count()

        form_data = {
            'name': f'{list(range(1, 150))}',
            'text': '1'
        }

        response = self.authorized_client.post('/message-templates/add/', data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        count_after = MessageTemplate.objects.count()
        self.assertTrue(count_before == count_after)

