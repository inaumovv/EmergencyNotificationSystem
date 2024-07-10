from contextlib import contextmanager

import pika

from services.DTOs.notification_dto import NotificationDTO
from website import settings


class RabbitMQPublisher:

    def __init__(
            self,
            exchange_name: str = 'default',
            queue_name: str = 'default',
            routing_key: str = ''
    ):
        self.exchange_name: str = exchange_name
        self.queue_name: str = queue_name
        self.routing_key: str = routing_key
        self.credentials = pika.PlainCredentials(username=settings.RABBITMQ_USER, password=settings.RABBITMQ_PASSWORD)
        self.parameters = pika.ConnectionParameters(host=settings.RABBITMQ_HOST, port=5672, credentials=self.credentials)
        self.create_queue_and_exchange()

    @contextmanager
    def get_channel(self):
        with pika.BlockingConnection(parameters=self.parameters).channel() as channel:
            yield channel

    def create_queue_and_exchange(self):
        with self.get_channel() as channel:
            queue = channel.queue_declare(queue=self.queue_name, durable=True)
            channel.exchange_declare(exchange=self.exchange_name, durable=True, exchange_type='fanout')
            channel.queue_bind(exchange=self.exchange_name, queue=queue.method.queue, routing_key=self.routing_key)

    def publish(self, data: NotificationDTO):
        with self.get_channel() as channel:
            channel.basic_publish(
                exchange=self.exchange_name,
                body=data.to_json(),
                routing_key=self.routing_key,
                properties=pika.BasicProperties(
                    delivery_mode=pika.DeliveryMode.Persistent
                )
            )
