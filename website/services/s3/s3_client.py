from contextlib import contextmanager, ContextDecorator

from botocore import session
from botocore.exceptions import NoCredentialsError, ClientError
from botocore.session import get_session, Session
from django.core.files import File

from website.settings import logger


class S3Client:
    def __init__(self, access_key: str, secret_key: str, endpoint_url: str, bucket_name: str):
        self.config: dict = {
            'aws_access_key_id': access_key,
            'aws_secret_access_key': secret_key,
            'endpoint_url': endpoint_url
        }
        self.bucket_name: str = bucket_name
        self.session: Session = get_session()

    @contextmanager
    def get_client(self):
        try:
            yield self.session.create_client('s3', **self.config)

        except ClientError as e:
            logger.error(e)

    def upload_file(self, file: bytes, s3_object_name: int):
        with self.get_client() as client:
            try:
                client.put_object(Bucket=self.bucket_name, Key=f'{s3_object_name}.xlsx', Body=file)

            except NoCredentialsError as e:
                logger.error(e)

            except ClientError as e:
                logger.error(e)

    def delete_file(self, s3_object_name: int):
        with self.get_client() as client:
            try:
                client.delete_object(Bucket=self.bucket_name, Key=f'{s3_object_name}.xlsx')

            except NoCredentialsError as e:
                logger.error(e)

            except ClientError as e:
                logger.error(e)

    def update_file(self, file: bytes, s3_object_name: int):
        try:
            self.delete_file(s3_object_name)
            self.upload_file(file, s3_object_name)

        except NoCredentialsError as e:
            logger.error(e)

        except ClientError as e:
            logger.error(e)

