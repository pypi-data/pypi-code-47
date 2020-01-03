from django.core.mail import send_mail
from django.template.loader import render_to_string

SENDER_EMAIL = 'SchoolApps <infoplan@katharineum.de>'


def send_mail_with_template(title, receivers, plain_template, html_template, context={}, sender_email=SENDER_EMAIL):
    msg_plain = render_to_string(plain_template, context)
    msg_html = render_to_string(html_template, context)

    try:
        send_mail(
            title,
            msg_plain,
            sender_email,
            receivers,
            html_message=msg_html,
        )
    except Exception as e:
        print("[EMAIL PROBLEM] ", e)
