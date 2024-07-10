import os

import requests
from dotenv import load_dotenv

from worker import settings

load_dotenv()

api_token = os.getenv('API_TOKEN')


class RequestsManager:

    @classmethod
    def put(cls, url: str, **data):
        requests.put(
            url=f'{settings.WEBSITE_ENDPOINT_URL}{url}',
            headers={'Authorization': f'Token {api_token}'},
            data=data
        )
