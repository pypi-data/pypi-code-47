from django.utils.module_loading import import_string

from .settings import (
    TRACK17_API_KEY,
    TRACK17_API_KEY_FUNCTION
)

__all__ = (
    'get_api_key',
)


def get_api_key():
    """
    Return api key
    """
    if TRACK17_API_KEY_FUNCTION:
        func = import_string(TRACK17_API_KEY_FUNCTION)
        if callable(func):
            return func()
    return TRACK17_API_KEY
