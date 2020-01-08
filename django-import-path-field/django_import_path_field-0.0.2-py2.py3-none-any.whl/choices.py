import six

from importpath_field.utils import import_string, get_path


class ImportPathChoices(list):
    def __init__(self, *objects, **kwargs):
        super(ImportPathChoices, self).__init__()
        self._registered = set()
        for obj in objects:
            if not isinstance(obj, (list, tuple)):
                obj = [obj]
            self._register(*obj)

    def _get_path(self, obj):
        if isinstance(obj, six.string_types):
            obj = import_string(obj)
        path = get_path(obj)
        return path

    def _get_description(self, obj):
        if isinstance(obj, six.string_types):
            obj = import_string(obj)

        if hasattr(obj, 'short_description'):
            return getattr(obj, 'short_description')
        if hasattr(obj, '__self__'):
            cls = obj.__self__
            if obj.__doc__:
                return obj.__doc__
            return '.'.join([cls.__name__, obj.__name__])
        return obj.__name__

    def _register(self, obj, description=None):
        path = self._get_path(obj)
        if path in self._registered:
            raise ValueError("Already registered")
        desc = description or self._get_description(obj)

        self.append([path, desc])
        self._registered.add(path)

    def register(self, description=None):
        """Decorator"""

        def wrap(obj):
            self._register(obj, description)
            return obj

        return wrap
