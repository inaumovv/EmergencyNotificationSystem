from django.db.models import Manager

from services.decorators.orm_decorators import set_fields


class BaseRepository:

    @classmethod
    @set_fields
    def get_objects(cls, object_: Manager, fields: list | tuple = None, **filters):
        return object_.filter(**filters).all() if filters else object_.all()

    @classmethod
    @set_fields
    def get_objects_with_relations(
            cls,
            object_: Manager,
            select_related: tuple | list,
            fields: list | tuple = None,
            **filters):
        if filters:
            return object_.select_related(*select_related).filter(**filters).all()
        return object_.select_related(*select_related).all()

    @classmethod
    def create_object(cls, object_: Manager, **data):
        return object_.create(**data)
