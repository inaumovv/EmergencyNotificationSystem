from celery import shared_task

from services.s3_client import S3Client
from website import settings
from website.celery import app

s3_client = S3Client(
    access_key=settings.AWS_ACCESS_KEY_ID,
    secret_key=settings.AWS_SECRET_ACCESS_KEY,
    endpoint_url=settings.ENDPOINT_URL,
    bucket_name='ens-container'
)


@shared_task(bind=True, default_retry_delay=5 * 60, time_limit=10)
def upload_file(self, file: bytes, s3_object_name: int):
    try:
        s3_client.upload_file(file, s3_object_name)
    except Exception as e:
        raise self.retry(exc=e)


@shared_task(bind=True, default_retry_delay=5 * 60, time_limit=10)
def delete_file(self, s3_object_name: int):
    try:
        s3_client.delete_file(s3_object_name)
    except Exception as e:
        raise self.retry(exc=e)


@shared_task(bind=True, default_retry_delay=5 * 60, time_limit=10)
def update_file(self, file, s3_object_name: int):
    try:
        s3_client.update_file(file, s3_object_name)
    except Exception as e:
        raise self.retry(exc=e)
