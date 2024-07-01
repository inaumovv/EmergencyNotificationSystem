from io import BytesIO

from botocore.response import StreamingBody

from services.file_parser import FileParser
from services.s3_client import S3Client
from services.smtp import send_mails
from worker import settings


class NotificationSender:
    s3_client: S3Client = S3Client(
        access_key=settings.AWS_ACCESS_KEY_ID,
        secret_key=settings.AWS_SECRET_ACCESS_KEY,
        endpoint_url=settings.ENDPOINT_URL,
        bucket_name='ens-container'
    )
    parser: FileParser = FileParser()

    @classmethod
    def send_notification(cls, data: dict):
        notification_id: int = data.get('notification_id')
        filename: str = data.get('filename')
        message: str = data.get('message_text')
        cls.__change_notification_status(notification_id, 'в обработке')
        contact_data: dict = cls.__get_contact_data(filename)
        cls.send_email(message, contact_data['email_addresses'])

    @classmethod
    def send_email(cls, message: str, email_addresses: list):
        send_mails(email_addresses, message)

    @classmethod
    def __get_contact_data(cls, filename: str):
        body: StreamingBody = cls.s3_client.download_file(filename)['Body']
        file: BytesIO = BytesIO(body.read())
        return cls.parser.parse_file(file)

    @classmethod
    def __change_notification_status(cls, notification_id: int, status: str):
        pass
