import os

import requests
from celery import shared_task

from dotenv import load_dotenv
from requests import Response

from rebalancer import settings
from rebalancer.settings import logger

load_dotenv()

api_token = os.getenv('API_TOKEN')

WEBSITE_URL = settings.WEBSITE_ENDPOINT_URL
WORKER_URL = settings.WORKER_ENDPOINT_URL


@shared_task(bind=True, default_retry_delay=5 * 60, time_limit=10)
def request_to_worker(self):
    try:
        response: Response = requests.post(
            url=f'{WORKER_URL}check/',
            headers={'Authorization': f'Token {api_token}'}
        )
        response.raise_for_status()

    except Exception as e:
        try:
            response: Response = requests.post(
                url=f'{WEBSITE_URL}notifications/return-to-queue/',
                headers={'Authorization': f'Token {api_token}'}
            )
            response.raise_for_status()
        except Exception as _e:
            self.retry(exc=_e)
            logger.error(_e)
            
        logger.error(e)
