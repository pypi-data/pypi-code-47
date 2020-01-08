from django.apps import AppConfig as BaseConfig
from django.utils.translation import ugettext_lazy as _


class ImportpathFieldConfig(BaseConfig):
    name = 'importpath_field'
    verbose_name = _('Importpath Field')
