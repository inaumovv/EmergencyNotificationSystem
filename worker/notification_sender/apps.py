from threading import Thread

from django.apps import AppConfig

from services.rabbitmq.rabbitmq_consumer import RabbitMQConsumer


class NotificationSenderConfig(AppConfig):
    consumer: RabbitMQConsumer = RabbitMQConsumer(queue_name='notifications', exchange_name='ens')
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notification_sender'

    def ready(self):
        Thread(target=self.consumer.start_consuming, daemon=True).start()
