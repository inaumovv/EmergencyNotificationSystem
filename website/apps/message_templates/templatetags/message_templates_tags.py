from django import template

from services.repositories.message_templates_repository import MessageTemplatesRepository

register = template.Library()


@register.simple_tag()
def get_message_templates():
    return MessageTemplatesRepository.get_all_message_templates(fields=('id', 'name', 'text'))

