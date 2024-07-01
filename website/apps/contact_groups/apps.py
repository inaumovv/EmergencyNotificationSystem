from django.apps import AppConfig


class ContactGroupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.contact_groups'
    verbose_name = 'Группа контактов'
    verbose_name_plural = 'Группы контактов'
