from contextlib import contextmanager
from typing import Generator

from botocore.client import BaseClient
from botocore.session import Session, get_session


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
        yield self.session.create_client('s3', **self.config)

    def download_file(self, filename: str):
        with self.get_client() as client:
            return client.get_object(Bucket=self.bucket_name, Key=f'{filename}.xlsx')
