# coding=utf-8
from django import template
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html

register = template.Library()


# @register.simple_tag
# def new_feedback_count():
#     from feedback.models import Feedback
#     count = Feedback.for_new().count()
#     if count > 0:
#         return format_html('<span style="color: #000000; margin-left: 10px; background: #EFB80B; padding: 1px 4px;'
#                            'font-size: 12px; border-radius: 4px;">{}</span>',
#                            count)
#     else:
#         return ''

