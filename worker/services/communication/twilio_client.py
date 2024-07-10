import logging
from contextlib import contextmanager

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from worker.settings import logger


class TwilioClient:

    def __init__(self, account_sid: str, auth_token: str, twilio_number: str):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_number = twilio_number

    @contextmanager
    def get_twilio_client(self):
        with Client(self.account_sid, self.auth_token) as client:
            yield client

    def send_message(self, phone_number: str, message: str):
        with self.get_twilio_client() as client:
            try:
                client.messages.create(body=message, from_=self.twilio_number, to=phone_number)

            except TwilioRestException as e:
                logger.error(f'Error sending message: {e}')

                if e.code == 21614:
                    logger.error('Invalid phone number')

                elif e.code == 20003:
                    logger.error('Insufficient balance on your Twilio account')

            except Exception as e:
                logger.error(f'Unknown error: {e}')
