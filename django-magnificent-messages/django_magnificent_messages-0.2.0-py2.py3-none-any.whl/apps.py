"""
django_magnificent_messages AppConfig
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoMagnificentMessagesConfig(AppConfig):
    name = 'django_magnificent_messages'
    verbose_name = _('Magnificent Messages')

    def ready(self):
        from . import conf  # noqa
