from datetime import datetime
from io import BytesIO

from botocore.response import StreamingBody

from services.file_parser import FileParser
from services.requests.request_manager import RequestsManager
from services.s3.s3_client import S3Client
from services.communication.smtp import send_mails
from services.communication.twilio_client import TwilioClient
from worker import settings
from .tasks import edit_notification


class NotificationSender:
    s3_client: S3Client = S3Client(
        access_key=settings.AWS_ACCESS_KEY_ID,
        secret_key=settings.AWS_SECRET_ACCESS_KEY,
        endpoint_url=settings.ENDPOINT_URL,
        bucket_name='ens-container'
    )
    twilio_client: TwilioClient = TwilioClient(
        account_sid=settings.TWILIO_ACCOUNT_SID,
        auth_token=settings.TWILIO_AUTH_TOKEN,
        twilio_number=settings.TWILIO_NUMBER
    )

    parser: FileParser = FileParser()
    requests: RequestsManager = RequestsManager

    @classmethod
    def send_notification(cls, data: dict):
        notification_id: int = data.get('notification_id')
        filename: str = data.get('filename')
        message: str = data.get('message_text')
        edit_notification.delay(notification_id, status='в обработке')
        contact_data: dict = cls.__get_contact_data(filename)
        send_mails(contact_data['email_addresses'], message)
        # cls.twilio_client.send_message(phone_number=contact_data['phone_number'], message=message)
        edit_notification.delay(notification_id, status='доставлено', delivery_time=datetime.now())

    @classmethod
    def __get_contact_data(cls, filename: str):
        body: StreamingBody = cls.s3_client.download_file(filename)['Body']
        file: BytesIO = BytesIO(body.read())
        return cls.parser.parse_file(file)

