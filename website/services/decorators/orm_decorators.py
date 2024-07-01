from django.db.models import QuerySet


def set_fields(func):
    def wrapper(*args, fields: tuple[str] | list[str] = None, **kwargs):
        if fields:
            return func(*args, **kwargs).values(*fields)
        return func(*args, **kwargs)

    return wrapper
