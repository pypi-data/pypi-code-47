# -*- coding: utf-8 -*-
from django.conf import settings
# from django.core.mail import send_mail
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage

from common.functions import send_mail_async
from common.views import BaseView
from .forms import *


# токен для невидимой капчи
def get_token(form):
    import logging
    from django.core.cache import cache
    logger = logging.getLogger(__name__)
    token = form.data.get('form_token', None)
    logger.info(u"POST token='" + token + "'")
    if token and token != cache.get('form_token'):
        cache.set('token', token, 10)
        logger.info(u"SAVE token='" + token + "'")
        return True
    else:
        logger.info(u"EQUAL TOKEN token='" + token + "'")
    return False


class FeedbackView(BaseView):
    email_subject = 'Сообщение с сайта WOODPSKOV.RU'
    form_message = 'Сообщение не отправлено!'
    form_success = False
    form_class = None
    form_name = None
    form_html = None

    def set_email_message(self, obj):
        form_fields = self.form_class.Meta.fields
        message = self.email_subject + '\n'
        message += 'Тема обращения (форма): ' + str(obj.get_subject_display()) + '\n'
        for field in form_fields:
            message += obj._meta.get_field(field).verbose_name.title() + ': ' + str(getattr(obj, field)) + '\n'
        return message

    def send_to_emails(self, obj):
        configs = FeedConfig.objects.filter(subject=obj.subject, is_active=True)
        message = self.set_email_message(obj)
        if configs:
            for conf in configs:
                emails = [e.strip() for e in filter(None, conf.email.split(','))]
                if emails:
                    send_mail_async(self.email_subject, message, emails, is_html=False)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid() and get_token(form):
            # if form.is_valid():
                try:
                    obj = form.save(commit=False)
                    obj.subject = form.subject
                    obj.save()
                    # self.handle_uploaded_file(request.FILES['file'])
                    self.send_to_emails(obj)
                    self.form_success = True
                    self.form_message = 'Сообщение отправлено!'
                except Exception as e:
                    print(e)
            self.form_html = render_to_string(form.template, {form.name: form}, request=request)

        return JsonResponse(dict(
            success=self.form_success,
            massage=self.form_message,
            form_name=self.form_name,
            form_html=self.form_html
        ))

    def handle_uploaded_file(self, file):
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        url = fs.url(filename)
        return url
