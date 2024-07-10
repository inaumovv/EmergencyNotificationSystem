from apps.contact_groups.models import ContactGroup
from services.repositories.base_repository import BaseRepository


class ContactGroupsRepository(BaseRepository):
    model: ContactGroup = ContactGroup

    @classmethod
    def get_all_contact_groups(cls, fields: list | tuple = None, **filters):
        return cls.get_objects(cls.model.objects, fields=fields, **filters)

