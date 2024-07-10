from django.core.mail import send_mail

from worker import settings


def send_mails(email_addresses: list, message: str):
    send_mail(
        subject='❗️❗️❗️Экстренное оповещение❗️❗️❗️',
        message=message,
        recipient_list=email_addresses,
        from_email=settings.EMAIL_HOST_USER
    )
