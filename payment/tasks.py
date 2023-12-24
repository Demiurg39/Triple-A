from io import BytesIO

import weasyprint
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from orders.models import Order


@shared_task
def payment_complete(order_id):
    """
    Async task to send notification
    on email if payment complete
    """
    order = Order.objects.get(id=order_id)

    subject = f"TripleA - Invoice no. {order.id}"
    message = "Please, find attached the invoice for your recent purchases"
    email = EmailMessage(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
    )
    html = render_to_string("order/orders/pdf.html", {"order": order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(
        f"order_{order.id}.pdf",
        out.getvalue(),
        "application/pdf",
    )
    email.send()
