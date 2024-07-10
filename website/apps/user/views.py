from django.contrib.auth.views import LoginView

from services.mixins.context_data_mixin import ContextDataMixin
from apps.user.forms import UserLoginForm


class UserLoginView(ContextDataMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'
    title_page = 'Вход'


