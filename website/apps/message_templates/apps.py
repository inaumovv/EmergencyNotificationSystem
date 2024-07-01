from django.apps import AppConfig


class MessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.message_templates'
    verbose_name = 'Шаблон сообщения'
    verbose_name_plural = 'Шаблоны сообщений'
