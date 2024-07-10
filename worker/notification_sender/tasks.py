from celery import shared_task

from services.requests.request_manager import RequestsManager
from worker.settings import logger


@shared_task(bind=True, default_retry_delay=5 * 60, time_limit=10)
def edit_notification(self, notification_id: int, **data):
    try:
        RequestsManager.put(url=f'update/{notification_id}/', **data)

    except Exception as e:
        logger.error(e)
        raise self.retry(exc=e)
