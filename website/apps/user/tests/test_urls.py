from services.tests.test_settings import Settings


class TestUsersURLS(Settings):

    def test_login_page_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)


