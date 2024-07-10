from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView, View

from apps.notifications.forms import NotificationTemplateForm
from apps.notifications.models import NotificationTemplate, SentNotification
from services.DTOs.notification_dto import NotificationDTO
from services.queues.rabbitmq_publisher import RabbitMQPublisher
from services.repositories.notification_templates_repository import NotificationTemplatesRepository
from services.repositories.sent_notifications_repository import SentNotificationsRepository

PAGE = 'notification_templates.html'


class AddNotificationTemplateView(LoginRequiredMixin, CreateView):
    template_name = PAGE
    form_class = NotificationTemplateForm
    success_url = reverse_lazy('notifications:templates_index')


class DeleteNotificationTemplateView(LoginRequiredMixin, DeleteView):
    template_name = PAGE
    success_url = reverse_lazy('notifications:templates_index')
    model: NotificationTemplate = NotificationTemplate


class EditNotificationTemplateView(LoginRequiredMixin, UpdateView):
    model: NotificationTemplate = NotificationTemplate
    template_name = PAGE
    form_class = NotificationTemplateForm
    success_url = reverse_lazy('notifications:templates_index')


class SentNotificationsView(LoginRequiredMixin, TemplateView):
    template_name = 'sent_notifications.html'


class SendNotificationView(LoginRequiredMixin, View):
    publisher: RabbitMQPublisher = RabbitMQPublisher(
        exchange_name='ens',
        queue_name='notifications'
    )

    def get(self, request, *args, **kwargs):
        notification_template_id: int = int(request.GET.get('notification_template_id'))

        try:
            notification_template: dict = NotificationTemplatesRepository.get_notification_templates_with_relations(
                select_related=('contact_group', 'message_template'),
                fields=('contact_group', 'message_template__text'),
                id=notification_template_id
            ).first()
            if not notification_template:
                raise ObjectDoesNotExist()

        except ObjectDoesNotExist:
            return HttpResponse(status=404)

        sent_notification: SentNotification = SentNotificationsRepository.create_sent_notification(
            notification_template_id
        )

        data: NotificationDTO = NotificationDTO(
            notification_id=sent_notification.id,
            message_text=notification_template['message_template__text'],
            filename=notification_template['contact_group']
        )

        self.publisher.publish(data)

        return redirect(reverse('notifications:sent_index'))
