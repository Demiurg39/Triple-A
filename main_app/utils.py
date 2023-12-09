from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_rental_key_email(email, key):
    subject = 'Ключ для аренды игры'
    message = render_to_string('email/rental_key_email.html', {'key': key})
    plain_message = strip_tags(message)

    try:
        send_mail(subject, plain_message, 'from@example.com', [email], html_message=message)
    except Exception as e:
        print(f"Ошибка при отправке email: {e}")
