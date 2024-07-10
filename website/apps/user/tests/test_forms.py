from apps.user.forms import UserLoginForm
from services.tests.test_settings import Settings


class TestLoginForm(Settings):

    def test_form_save(self):
        form_data = {'username': 'Name', 'password': 'Password'}
        form: UserLoginForm = UserLoginForm(data=form_data)
        self.assertTrue(form.is_valid())


