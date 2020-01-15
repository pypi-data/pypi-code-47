from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ConfigConfig(AppConfig):
    name = 'common.config'
    verbose_name = _('Настройки сайта')
