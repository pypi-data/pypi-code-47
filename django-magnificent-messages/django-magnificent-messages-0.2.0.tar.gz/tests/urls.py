import json

from django import forms
import django_magnificent_messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template import engines
from django.template.response import TemplateResponse
from django.urls import path, re_path, reverse
from django.views.decorators.cache import never_cache
from django.views.generic.edit import FormView

NOTIFICATIONS_TEMPLATE = """{% if dmm %}
<ul class="notifications">
    {% for notification in dmm.notifications.all %}
    <li{% if notification.level_tag %} class="{{ notification.level_tag }}"{% endif %}>
        {{ notification.text }}
    </li>
    {% endfor %}
</ul>
{% endif %}
"""

MESSAGES_TEMPLATE = """
all: {{ dmm.messages.all_count }}<br>
read: {{ dmm.messages.read_count }}<br>
unread: {{ dmm.messages.unread_count }}<br>
archived: {{ dmm.messages.archived_count }}<br>
new: {{ dmm.messages.new_count }}<br>
{% if show_new == 1 %}
<ul>
{% for msg in dmm.messages.new %}
<li>{{ msg.text }}</li>
{% endfor %}
</ul>
{% endif %}
"""


@never_cache
def notifications_add(request, message_type):
    # Don't default to False here to test that it defaults to False if
    # unspecified.
    fail_silently = request.POST.get('fail_silently', None)
    for msg in request.POST.getlist('notifications'):
        if fail_silently is not None:
            getattr(django_magnificent_messages.notifications, message_type)(request, msg, fail_silently=fail_silently)
        else:
            getattr(django_magnificent_messages.notifications, message_type)(request, msg)
    return HttpResponseRedirect(reverse('show_notification'))


@never_cache
def messages_add(request, message_type):
    data = json.loads(request.body.decode('utf8'))
    for msg in data['messages']:
        getattr(django_magnificent_messages.messages, message_type)(request, **msg)
    return HttpResponseRedirect(reverse('messages_show', args=(data.get('show_new', 0),)))


@never_cache
def system_messages_add(request, message_type):
    data = json.loads(request.body.decode('utf8'))
    for msg in data['messages']:
        getattr(django_magnificent_messages.system_messages, message_type)(request, **msg)
    return HttpResponseRedirect(reverse('messages_show', args=(data.get('show_new', 0),)))


@never_cache
def notifications_add_template_response(request, message_type):
    for msg in request.POST.getlist('messages'):
        getattr(django_magnificent_messages.notifications, message_type)(request, msg)
    return HttpResponseRedirect(reverse('show_template_response_notification'))


@never_cache
def notifications_show(request):
    template = engines['django'].from_string(NOTIFICATIONS_TEMPLATE)
    return HttpResponse(template.render(request=request))


@never_cache
def messages_show(request, show_new):
    template = engines['django'].from_string(MESSAGES_TEMPLATE)
    return HttpResponse(template.render(request=request, context={"show_new": show_new}))


@never_cache
def show_template_response_notification(request):
    template = engines['django'].from_string(NOTIFICATIONS_TEMPLATE)
    return TemplateResponse(request, template)


urlpatterns = [
    re_path('^notifications_add/(secondary|primary|info|success|warning|error)/$', notifications_add,
            name='add-notification'),
    path('notifications_show/', notifications_show, name='show_notification'),
    re_path('^messages_add/(secondary|primary|info|success|warning|error)/$', messages_add,
            name='add-message'),
    re_path('^system_messages_add/(secondary|primary|info|success|warning|error)/$', system_messages_add,
            name='add-system-message'),
    path('messages_show/<int:show_new>', messages_show, name="messages_show"),
    path('notifications_show/', notifications_show, name='show_notification'),
    re_path(
        '^template_response/notifications_add/(secondary|primary|info|success|warning|error)/$',
        notifications_add_template_response, name='notifications_add_template_response',
    ),
    path('template_response/notifications_show/', show_template_response_notification,
         name='show_template_response_notification'),
]
