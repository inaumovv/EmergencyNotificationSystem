from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey

from apps.contact_groups.models import ContactGroup
from apps.message_templates.models import MessageTemplate


class NotificationTemplate(models.Model):
    name = models.CharField(max_length=122, unique=True, verbose_name='Название')
    contact_group = ForeignKey(
        ContactGroup,
        on_delete=models.CASCADE,
        verbose_name="Группа контактов",
        related_name="notification_templates")
    message_template = ForeignKey(
        MessageTemplate,
        on_delete=models.CASCADE,
        verbose_name="Сообщение",
        related_name="notification_templates"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шаблон оповещения'
        verbose_name_plural = 'Шаблоны оповещений'
        ordering = ('created_at',)


class SentNotification(models.Model):
    class Status(models.TextChoices):
        IN_QUEUE = "в очереди", "в очереди"
        IN_PROCESSING = "в обработке", "в обработке"
        DELIVERED = "доставлено", "доставлено"

    notification_template = models.ForeignKey(
        NotificationTemplate,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Шаблон оповещения",
        related_name="notifications"
    )
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.IN_QUEUE,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    delivery_time = models.DateTimeField(null=True, blank=True, verbose_name="Время доставки")

    def __str__(self):
        return f'{self.id} | {self.status} | {self.created_at}'

    class Meta:
        verbose_name = "Оповещение"
        verbose_name_plural = "Оповещения"
        ordering = ('created_at',)
