from django.test import Client

from services.tests.test_settings import Settings


class TestUsersViews(Settings):

    def setUp(self):
        self.test_client = Client()

    def test_login_view(self):
        data = {'username': 'Name', 'password': 'Password'}
        response = self.test_client.post('/login/', data=data)
        self.assertEqual(response.status_code, 200)
