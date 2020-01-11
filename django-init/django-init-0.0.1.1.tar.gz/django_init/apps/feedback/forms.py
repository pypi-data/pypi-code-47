# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import *


class QuestionForm(forms.ModelForm):
    name = 'question_form'
    subject = SUBJ_QST
    template = 'feedback/forms/question.html'

    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'email', 'message', 'file']
        labels = {
            'name': '',
            'phone': '',
            'email': '',
            'message': '',
            'file': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваше имя')}),
            'phone': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваш телефон')}),
            'email': forms.EmailInput(attrs={'required': False, 'placeholder': _(u'Ваш E-mail')}),
            'message': forms.Textarea(attrs={'required': True, 'rows': 5, 'placeholder': _(u'Ваш вопрос')}),
        }


class OrderModalForm(forms.ModelForm):
    name = 'order_modal_form'
    subject = SUBJ_ORDER
    template = 'feedback/forms/modal-order.html'

    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'email', 'message']
        labels = {
            'name': '',
            'phone': '',
            'email': '',
            'message': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваше имя')}),
            'phone': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваш телефон')}),
            'email': forms.EmailInput(attrs={'required': False, 'placeholder': _(u'Ваш E-mail')}),
            'message': forms.Textarea(attrs={'required': True, 'rows': 5, 'placeholder': _(u'Ваш вопрос')}),
        }


class CallForm(forms.ModelForm):
    name = 'call_form'
    subject = SUBJ_CALL
    template = 'feedback/forms/call.html'

    class Meta:
        model = Feedback
        fields = ['name', 'phone']
        labels = {
            'name': '',
            'phone': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваше имя'), 'class': 'user-name'}),
            'phone': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваш телефон'), 'class': 'user-number'}),
        }


class CallModalForm(forms.ModelForm):
    name = 'call_modal_form'
    subject = SUBJ_CALL
    template = 'feedback/forms/modal-call.html'

    class Meta:
        model = Feedback
        fields = ['name', 'phone']
        labels = {
            'name': '',
            'phone': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваше имя')}),
            'phone': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваш телефон')}),
        }


class AppointmentForm(forms.ModelForm):
    form_name = "appointment"

    class Meta:
        model = Feedback
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваше имя')}),
            'phone': forms.TextInput(attrs={'required': True, 'placeholder': _(u'Ваш телефон')}),
        }
