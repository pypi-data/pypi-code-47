from django.db import models

from .descriptors import ProxyFieldDescriptor, ImportPathProxy
from ..utils import get_path


class ImportPathField(models.CharField):
    def __init__(self, verbose_name=None, name=None,
                 **kwargs):
        kwargs.setdefault('max_length', 256)
        super(ImportPathField, self).__init__(verbose_name, name, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super(ImportPathField, self).contribute_to_class(cls, name, **kwargs)
        setattr(cls, self.name, ProxyFieldDescriptor(self))

    def get_prep_value(self, value):
        if isinstance(value, ImportPathProxy):
            return value.path
        if not isinstance(value, str):
            return get_path(value)
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        return self.get_prep_value(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        if hasattr(value, 'value'):
            return value.value
        return value

    def to_python(self, value):
        if isinstance(value, ImportPathProxy):
            return value
        else:
            return super(ImportPathField, self).to_python(value)
