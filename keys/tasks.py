from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

email_from = settings.DEFAULT_FROM_EMAIL


@shared_task
def send_rental_key_email(email, key):
    subject = "Ключ для аренды игры"
    message = render_to_string("email/rental_key_email.html", {"key": key})
    plain_message = strip_tags(message)

    return send_mail(
        subject,
        plain_message,
        email_from,
        [email],
        html_message=message,
    )
