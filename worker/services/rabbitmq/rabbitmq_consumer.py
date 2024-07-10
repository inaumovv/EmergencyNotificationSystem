import json
from contextlib import contextmanager

import pika

from notification_sender.notification_sender import NotificationSender
from worker import settings


class RabbitMQConsumer:

    def __init__(self, exchange_name: str = 'default', queue_name: str = 'default', routing_key: str = ''):
        self.queue_name: str = queue_name
        self.exchange_name: str = exchange_name
        self.routing_key: str = routing_key
        self.credentials = pika.PlainCredentials(username=settings.RABBITMQ_USER, password=settings.RABBITMQ_PASSWORD)
        self.parameters = pika.ConnectionParameters(host=settings.RABBITMQ_HOST, port=5672,
                                                    credentials=self.credentials)

    @contextmanager
    def get_channel(self):
        with pika.BlockingConnection(parameters=self.parameters).channel() as channel:
            yield channel

    def create_queue_and_exchange(self):
        with self.get_channel() as channel:
            queue = channel.queue_declare(queue=self.queue_name, durable=True)
            channel.exchange_declare(exchange=self.exchange_name, durable=True, exchange_type='fanout')
            channel.queue_bind(exchange=self.exchange_name, queue=queue.method.queue, routing_key=self.routing_key)

    def start_consuming(self):
        with self.get_channel() as channel:
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback)
            channel.start_consuming()

    @staticmethod
    def callback(channel, method, properties, body):
        data = json.loads(body)
        NotificationSender.send_notification(data)
        channel.basic_ack(delivery_tag=method.delivery_tag)
