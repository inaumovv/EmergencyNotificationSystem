from django.apps import AppConfig

from services.rabbitmq_consumer import RabbitMQConsumer


class NotificationSenderConfig(AppConfig):
    consumer: RabbitMQConsumer = RabbitMQConsumer(queue_name='notifications')
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notification_sender'

    def ready(self):
        self.consumer.start_consuming()
