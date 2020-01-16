from django.http import HttpRequest

from .backend import MessageBackend
from . import constants

__all__ = (
    'add', 'get',
    'secondary', 'primary', 'info', 'success', 'warning', 'error',
)


class NotificationFailure(Exception):
    pass


def add(request: HttpRequest, level: int, text: str, subject: str = None, extra=None,
        fail_silently: bool = False) -> None:
    """
    Attempt to notifications_add a notification to the request using the 'django_magnificent_messages' app.
    """
    try:
        backend = request.dmm_backend  # type: MessageBackend
    except AttributeError:
        if not isinstance(request, HttpRequest):
            raise TypeError(
                "add() argument must be an HttpRequest object, not "
                "'%s'." % request.__class__.__name__
            )
        if not fail_silently:
            raise NotificationFailure(
                'You cannot add notifications without installing '
                'django_magnificent_messages.middleware.MessageMiddleware'
            )
    else:
        return backend.add_notification(level, text, subject, extra)


def get(request: HttpRequest):
    """
    Return the notifications on the request if it exists, otherwise return
    an empty list.
    """
    try:
        return request.dmm_backend.notifications
    except AttributeError:
        return []


def count(request: HttpRequest):
    """
    Return notifications count on the request if exist, otherwise return 0
    """
    try:
        return request.dmm_backend.notifications_count
    except AttributeError:
        return 0


def secondary(request: HttpRequest, text: str, subject: str = None, extra=None, fail_silently: bool = False) -> None:
    """Add a notification with the ``SECONDARY`` level."""
    add(request, constants.SECONDARY, text, subject, extra=extra, fail_silently=fail_silently)


def primary(request: HttpRequest, text: str, subject: str = None, extra=None, fail_silently: bool = False) -> None:
    """Add a notification with the ``PRIMARY`` level."""
    add(request, constants.PRIMARY, text, subject, extra=extra, fail_silently=fail_silently)


def info(request: HttpRequest, text: str, subject: str = None, extra=None, fail_silently: bool = False) -> None:
    """Add a notification with the ``INFO`` level."""
    add(request, constants.INFO, text, subject, extra=extra, fail_silently=fail_silently)


def success(request: HttpRequest, text: str, subject: str = None, extra=None, fail_silently: bool = False) -> None:
    """Add a notification with the ``SUCCESS`` level."""
    add(request, constants.SUCCESS, text, subject, extra=extra, fail_silently=fail_silently)


def warning(request: HttpRequest, text: str, subject: str = None, extra=None, fail_silently: bool = False) -> None:
    """Add a notification with the ``WARNING`` level."""
    add(request, constants.WARNING, text, subject, extra=extra, fail_silently=fail_silently)


def error(request: HttpRequest, text: str, subject: str = None, extra=None, fail_silently: bool = False) -> None:
    """Add a notification with the ``ERROR`` level."""
    add(request, constants.ERROR, text, subject, extra=extra, fail_silently=fail_silently)
