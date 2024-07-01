import uuid

from django.contrib.auth.models import User
from django.db import models


def default_uid():
    pass


class ContactGroup(models.Model):
    group_name = models.CharField(max_length=122, unique=True, verbose_name='Название')
    filename = models.CharField(max_length=122, default='default', verbose_name='Имя объекта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'Группа контактов'
        verbose_name_plural = 'Группы контактов'
        ordering = ('created_at',)
