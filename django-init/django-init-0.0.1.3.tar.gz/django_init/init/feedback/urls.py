# coding=utf-8

from django.conf.urls import url
from . import views

from .forms import *
from .views import FeedbackView

app_name = 'feedback'

urlpatterns = [
    url(r'^send_call$', FeedbackView.as_view(form_class=CallForm), name='call_form'),
    url(r'^send_modal_call$', FeedbackView.as_view(form_class=CallModalForm), name='call_modal_form'),
    url(r'^send_question$', FeedbackView.as_view(form_class=QuestionForm), name='question_form'),
    url(r'^send_order_modal$', FeedbackView.as_view(form_class=OrderModalForm), name='order_modal_form'),
]
