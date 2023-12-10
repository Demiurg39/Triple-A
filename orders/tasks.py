from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created(order_id):
    """Task send email if order was successfully created"""
    order = Order.objects.get(id=order_id)
    subject = f"Order #{order_id}"
    message = f"Dear {order.first_name},\n\n\
            You have successfully placed an order.\n\
            You're order ID is - {order_id}"

    mail_sent = send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
    )
    return mail_sent
