from services.tests.test_settings import Settings


class TestNotificationsURLS(Settings):

    def test_templates_index_url(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/login/?next=/')

    def test_templates_add_url(self):
        response = self.client.post('/add/')
        self.assertRedirects(response, '/login/?next=/add/')

    def test_templates_delete_url(self):
        response = self.client.post('/delete/2/')
        self.assertRedirects(response, '/login/?next=/delete/2/')

    def test_templates_edit_url(self):
        response = self.client.post('/edit/2/')
        self.assertRedirects(response, '/login/?next=/edit/2/')

    def test_sent_index(self):
        response = self.client.get('/sent-notifications/')
        self.assertRedirects(response, '/login/?next=/sent-notifications/')

    def test_send_notification(self):
        response = self.client.get('/send/')
        self.assertRedirects(response, '/login/?next=/send/')