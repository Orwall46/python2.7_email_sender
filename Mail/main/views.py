# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import string
import random
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import ListEmail, ReadMail
from .task import send_mail_func


def get_short_code():
    '''Return short code for mail'''
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        return short_id


def index(request):
    '''A home page with out Celery.'''
    context = {}
    if request.POST:
        text = request.POST['text']
        # emails = [x.email for x in ListEmail.objects.all()]
        users = ListEmail.objects.all()
        try:
            for user in users:
                id_read = get_short_code()
                data = {
                    'text': text,
                    'name': user.name,
                    'birthday': user.birthday,
                    'id': id_read
                }
                html_body = render_to_string('emails_templates/template.html', data)
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
            context['success'] = 1
        except Exception as ex:
            print(ex)
            context['success'] = 0
    return render(request, 'index.html', context=context)


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Done!")


def read_mail(request):
    if 'id' in request.GET:
        code_id = request.GET['id']
        try:
            read = ReadMail.objects.get(code=code_id)
            read.is_read = True
            read.save()
        except:
            print('Oopps...')
    image_data = open("media/django.png", 'rb').read()
    return HttpResponse(image_data, content_type="image/png")
