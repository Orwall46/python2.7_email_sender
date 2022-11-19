# -*- coding: utf-8 -*-
from __future__ import absolute_import


import string
import random
from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import ListEmail, ReadMail


@shared_task(bind=True)
def send_mail_func(self):
    users = ListEmail.objects.all()
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    try:
        for user in users:
            id_read = ''.join(random.choice(char) for x in range(length))
            data = {
                'name': user.name,
                'birthday': user.birthday,
                'id': id_read
            }
            html_body = render_to_string('emails_templates/celery_templete.html', data)
            msg = EmailMultiAlternatives(
                subject="Hello world",
                from_email=settings.EMAIL_HOST_USER,
                to=[user.email]
            )
            msg.attach_alternative(html_body, "text/html")
            msg.send()
            ReadMail.objects.create(
                user=user,
                code=id_read,
                url='http://127.0.0.1:8000/media/django.png?id={}'.format(id_read)
                )
    except Exception as ex:
        print(ex)
    return 'Done'
