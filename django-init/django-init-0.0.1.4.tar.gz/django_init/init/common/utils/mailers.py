from __future__ import unicode_literals
from ..decorators import run_async
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.exceptions import ImproperlyConfigured
from config.models import Config
from django.template.loader import get_template


def send_html_mail(subject, message, recipients, is_html):

    if not hasattr(settings, 'EMAIL_HOST') or not hasattr(settings, 'EMAIL_PORT'):
        raise ImproperlyConfigured('Email server configurations not found in settings.py.')

    from_email = settings.EMAIL_HOST_USER
    msg = EmailMessage(subject, message, from_email, recipients)
    if is_html:
        msg.content_subtype = 'html'
    msg.send(fail_silently=True)


# def send_mail(subject, message, to_email, recipients, is_html, **kwargs):
#     sys_config = Config.get_configs()
#
#     if 'SITE_NAME' not in sys_config or 'DOMAIN' not in sys_config:
#         raise ImproperlyConfigured('SITE_NAME and DOMAIN not found. It should be defined in System Configurations')
#
#     if not hasattr(settings, 'EMAIL_HOST') or not hasattr(settings, 'EMAIL_PORT'):
#         raise ImproperlyConfigured('Email server configurations not found in settings.py.')
#
#     # from_email = '%s <noreply@%s>' % (sys_config['SITE_NAME'], sys_config['DOMAIN'])
#     from_email = settings.EMAIL_HOST_USER
#     msg = EmailMessage(subject, message, from_email, to_email, recipients)
#
#     if 'attach' in kwargs and kwargs['attach']:
#         attach = kwargs['attach']
#         msg.attach(attach['filename'], attach['content'], attach['mimetype'])
#     # is_html - флаг, чтобы передавать html-файл
#     if is_html:
#         msg.content_subtype = "html"
#     # fail_silently=True - if exception no send
#     msg.send()
#     print('SEND to e-mail %s' % to_email)
#

# @run_async
# def send_mail_data(data, **kwargs):
#     s_email = data['emails'] if 'emails' in data else ''
#     on_email = data['email'] if 'email' in data and data['email'] not in s_email else ''
#
#     msg_subj = data['subject'] if 'subject' in data else ''
#     msg_base = data['result_message'] if 'result_message' in data else ''
#     msg_html = data['html'] if 'html' in data else ''
#     if msg_base == msg_html:
#         msg_html = ''
#     to_email = [x.strip() for x in on_email.split(',')] if on_email else ''
#     recipients = [x.strip() for x in s_email.split(',')] if s_email else ''
#
#     context = {'data': data, 'TITLE': msg_subj, 'MESSAGE': msg_base, 'MESSAGE_HTML': msg_html,
#                'SITE_NAME': Config.get_site_name(), 'DOMAIN': Config.get_domain(), 'CONFIG': Config.get_configs()}
#
#     msg_text = get_template("feedback/mail.html").render(context)
#     msg_subj = msg_subj if msg_subj else get_template("feedback/mail_subject.txt").render(context)
#     recipients = recipients if recipients else [x.strip() for x in Config.get_email_to().split(',')]
#     if hasattr(settings, 'TEST_EMAIL_TO') and settings.TEST_EMAIL_TO:
#         to_email = [settings.TEST_EMAIL_TO]
#         recipients = None
#     if to_email:
#         for x in to_email:
#             send_mail(msg_subj, msg_text, [x], '', True, **kwargs) if x else None
#     if recipients:
#         for y in recipients:
#             send_mail(msg_subj, msg_text, [y], '', True, **kwargs) if y else None

