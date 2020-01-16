from typing import Iterable

from django.http import HttpRequest

from django_magnificent_messages.messages import MessageFailure
from .backend import MessageBackend
from . import constants

__all__ = (
    'add', 'secondary', 'primary', 'info', 'success', 'warning', 'error',
)


def add(request: HttpRequest,
        level: int = constants.SECONDARY,
        text: str = None,
        subject: str = None,
        extra: object = None,
        to_users_pk: Iterable = tuple(),
        to_groups_pk: Iterable = tuple(),
        fail_silently: bool = False,
        html_safe: bool = False,
        reply_to_pk=None) -> None:
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
            raise MessageFailure(
                'You cannot add messages without installing '
                'django_magnificent_messages.middleware.MessageMiddleware'
            )
    else:
        return backend.send_message(level, text, subject, extra, to_users_pk, to_groups_pk, False, html_safe,
                                    reply_to_pk)


def secondary(request: HttpRequest,
              text: str,
              subject: str = None,
              extra: object = None,
              to_users_pk: Iterable = tuple(),
              to_groups_pk: Iterable = tuple(),
              fail_silently: bool = False,
              html_safe: bool = False,
              reply_to_pk=None) -> None:
    """Add a message with the ``SECONDARY`` level."""
    add(request, constants.SECONDARY, text, subject, extra, to_users_pk, to_groups_pk, fail_silently, html_safe,
        reply_to_pk)


def primary(request: HttpRequest,
            text: str,
            subject: str = None,
            extra: object = None,
            to_users_pk: Iterable = tuple(),
            to_groups_pk: Iterable = tuple(),
            fail_silently: bool = False,
            html_safe: bool = False,
            reply_to_pk=None) -> None:
    """Add a message with the ``PRIMARY`` level."""
    add(request, constants.PRIMARY, text, subject, extra, to_users_pk, to_groups_pk, fail_silently, html_safe,
        reply_to_pk)


def info(request: HttpRequest,
         text: str,
         subject: str = None,
         extra: object = None,
         to_users_pk: Iterable = tuple(),
         to_groups_pk: Iterable = tuple(),
         fail_silently: bool = False,
         html_safe: bool = False,
         reply_to_pk=None) -> None:
    """Add a message with the ``INFO`` level."""
    add(request, constants.INFO, text, subject, extra, to_users_pk, to_groups_pk, fail_silently, html_safe, reply_to_pk)


def success(request: HttpRequest,
            text: str,
            subject: str = None,
            extra: object = None,
            to_users_pk: Iterable = tuple(),
            to_groups_pk: Iterable = tuple(),
            fail_silently: bool = False,
            html_safe: bool = False,
            reply_to_pk=None) -> None:
    """Add a message with the ``SUCCESS`` level."""
    add(request, constants.SUCCESS, text, subject, extra, to_users_pk, to_groups_pk, fail_silently, html_safe,
        reply_to_pk)


def warning(request: HttpRequest,
            text: str,
            subject: str = None,
            extra: object = None,
            to_users_pk: Iterable = tuple(),
            to_groups_pk: Iterable = tuple(),
            fail_silently: bool = False,
            html_safe: bool = False,
            reply_to_pk=None) -> None:
    """Add a message with the ``WARNING`` level."""
    add(request, constants.WARNING, text, subject, extra, to_users_pk, to_groups_pk, fail_silently, html_safe,
        reply_to_pk)


def error(request: HttpRequest,
          text: str,
          subject: str = None,
          extra: object = None,
          to_users_pk: Iterable = tuple(),
          to_groups_pk: Iterable = tuple(),
          fail_silently: bool = False,
          html_safe: bool = False,
          reply_to_pk=None) -> None:
    """Add a message with the ``ERROR`` level."""
    add(request, constants.ERROR, text, subject, extra, to_users_pk, to_groups_pk, fail_silently, html_safe,
        reply_to_pk)
