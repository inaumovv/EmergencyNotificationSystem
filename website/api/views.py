from django.db.models import QuerySet
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import NotificationSerializer
from services.DTOs.notification_dto import NotificationDTO
from services.queues.rabbitmq_publisher import RabbitMQPublisher
from services.repositories.sent_notifications_repository import SentNotificationsRepository


class NotificationUpdateAPIView(UpdateAPIView):
    permission_classes: tuple = (IsAuthenticated,)
    serializer_class: NotificationSerializer = NotificationSerializer
    queryset: QuerySet = SentNotificationsRepository.get_sent_notifications()


class ReturnNotificationToQueueAPIView(APIView):
    publisher: RabbitMQPublisher = RabbitMQPublisher(
        exchange_name='ens',
        queue_name='notifications'
    )
    repo: SentNotificationsRepository = SentNotificationsRepository
    permission_classes: tuple = (IsAuthenticated,)

    def post(self, request: Request):
        in_processing_notifications = self.repo.get_sent_notifications_with_relations(
            select_related=('notification_template__contact_group', 'notification_template__message_template'),
            fields=('id', 'notification_template__contact_group', 'notification_template__message_template__text')
        )

        if in_processing_notifications:
            for notification in in_processing_notifications:
                data: NotificationDTO = NotificationDTO(
                    notification_id=notification['id'],
                    message_text=notification['notification_template__message_template__text'],
                    filename=notification['notification_template__contact_group']
                )

                self.publisher.publish(data)

        return Response(status=status.HTTP_200_OK)
