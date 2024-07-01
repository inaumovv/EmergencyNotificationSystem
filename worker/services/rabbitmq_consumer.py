import json
from contextlib import contextmanager

import pika

from notification_sender.notification_sender import NotificationSender


class RabbitMQConsumer:

    def __init__(self, host: str = 'localhost', queue_name: str = 'default'):
        self.host: str = host
        self.queue_name: str = queue_name

    @contextmanager
    def get_channel(self):
        with pika.BlockingConnection(pika.ConnectionParameters(host=self.host)).channel() as channel:
            yield channel

    def start_consuming(self):
        with self.get_channel() as channel:
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue='notifications', on_message_callback=self.callback)
            channel.start_consuming()

    @staticmethod
    def callback(channel, method, properties, body):
        data = json.loads(body)
        NotificationSender.send_notification(data)
        channel.basic_ack(delivery_tag=method.delivery_tag)
