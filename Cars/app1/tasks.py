from celery import shared_task
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.template.loader import get_template


UserModel = get_user_model()

@shared_task
def send_mail_task(user_id):
    data  = UserModel.objects.get(id=user_id)
    ctx={
        'user': data.username,
        'first_name': data.first_name,
        'last_name': data.last_name            
        }
    message = get_template('index.html').render(ctx)
    msg = EmailMessage(
        'Registration',
        message,
        'panchalvishal2710@gmail.com',
        [data.email],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return None