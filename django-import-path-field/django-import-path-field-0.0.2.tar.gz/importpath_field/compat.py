import six

try:
    from django.utils.module_loading import import_string # noqa
except ImportError:
    from django.utils.module_loading import import_by_path as import_string # noqa


try:

    ModuleNotFoundError = ModuleNotFoundError
except NameError:
    # python 3.5
    ModuleNotFoundError = ImportError

__all__ = ['import_string', ModuleNotFoundError]
