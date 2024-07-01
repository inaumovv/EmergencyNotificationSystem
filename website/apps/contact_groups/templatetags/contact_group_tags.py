from django import template

from services.repositories.contact_groups_repository import ContactGroupsRepository

register = template.Library()


@register.simple_tag
def get_contact_groups():
    return ContactGroupsRepository.get_all_contact_groups(fields=('id', 'group_name', 'filename'))
