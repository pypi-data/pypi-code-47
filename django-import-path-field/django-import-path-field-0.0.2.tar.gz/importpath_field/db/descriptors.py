import six

from importpath_field.utils import import_string, get_path


class ImportPathProxy(object):
    def __init__(self, instance, field_name):
        self.instance = instance
        self.field_name = field_name

    # def __repr__(self):
    #     return '<path={self.path}>'.format(self=self)

    def get_path(self):
        return self.instance.__dict__[self.field_name]

    def set_path(self, value):
        self.instance.__dict__[self.field_name] = value

    path = property(get_path, set_path)

    def get_object(self):
        return import_string(self.path)

    def set_object(self, value):
        if not isinstance(value, six.text_type):
            value = get_path(value)
        self.path = value

    resolve = property(get_object)


class ProxyFieldDescriptor(object):
    def __init__(self, field, proxy_class=ImportPathProxy):
        self.field = field
        self.field_name = field.name
        self.proxy_class = proxy_class
        self.field = field

    def __get__(self, instance=None, owner=None):
        # grab the original value before we proxy
        if instance is None:
            return self

        if self.field_name not in instance.__dict__:
            return None
        value = instance.__dict__[self.field_name]
        if value is None:
            # We can't proxy a None through a unicode sub-class
            return value
        return self.proxy_class(instance=instance, field_name=self.field_name)

    def __set__(self, instance, value):
        self.proxy_class(
            instance=instance,
            field_name=self.field_name
        ).set_object(value)
