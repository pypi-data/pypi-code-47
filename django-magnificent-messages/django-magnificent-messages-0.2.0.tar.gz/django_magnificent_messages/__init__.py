from django_magnificent_messages.backend import MessageBackend
from .constants import *
from . import notifications, messages, system_messages


def get_level(request):
    """
    Return the minimum level of messages to be recorded.

    The default level is the ``DMM_MINIMAL_LEVEL`` setting. If this is not found,
    use the ``INFO`` level.
    """
    dmm_backend = getattr(request, 'dmm_backend', MessageBackend(request))  # type: MessageBackend
    return dmm_backend.get_level()


def set_level(request, level):
    """
    Set the minimum level of messages to be recorded, and return ``True`` if
    the level was recorded successfully.

    If set to ``None``, use the default level (see the get_level() function).
    """
    if not hasattr(request, 'dmm_backend'):
        return False
    request.dmm_backend.set_level(level)
    return True

