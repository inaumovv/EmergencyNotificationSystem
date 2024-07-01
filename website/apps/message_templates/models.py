from django.contrib.auth.models import User
from django.db import models


class MessageTemplate(models.Model):
    name = models.CharField(max_length=122, unique=True, verbose_name='Сообщение')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('created_at',)

