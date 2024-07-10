from services.tests.test_settings import Settings


class TestContactGroupsURLS(Settings):

    def test_index_url(self):
        response = self.client.get('/contact-groups/')
        self.assertRedirects(response, '/login/?next=/contact-groups/')

    def test_add_url(self):
        response = self.client.post('/contact-groups/add/')
        self.assertRedirects(response, '/login/?next=/contact-groups/add/')

    def test_delete_url(self):
        response = self.client.post('/contact-groups/delete/2/')
        self.assertRedirects(response, '/login/?next=/contact-groups/delete/2/')

    def test_edit_url(self):
        response = self.client.post('/contact-groups/edit/2/')
        self.assertRedirects(response, '/login/?next=/contact-groups/edit/2/')
