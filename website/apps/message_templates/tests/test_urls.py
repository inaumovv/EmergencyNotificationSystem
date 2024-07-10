from services.tests.test_settings import Settings


class TestMessageTemplatesUrls(Settings):

    def test_index_url(self):
        response = self.client.get('/message-templates/')
        self.assertRedirects(response, '/login/?next=/message-templates/')

    def test_add_url(self):
        response = self.client.post('/message-templates/add/')
        self.assertRedirects(response, '/login/?next=/message-templates/add/')

    def test_delete_url(self):
        response = self.client.post('/message-templates/delete/2/')
        self.assertRedirects(response, '/login/?next=/message-templates/delete/2/')

    def test_edit_url(self):
        response = self.client.post('/message-templates/edit/2/')
        self.assertRedirects(response, '/login/?next=/message-templates/edit/2/')


