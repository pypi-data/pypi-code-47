from typing import Iterable

from django.http import HttpRequest

from .backend import MessageBackend
from . import constants

__all__ = (
    'all', 'all_count', 'read', 'read_count', 'unread', 'unread_count', 'archived', 'archived_count', 'new',
    'new_count',
    'add', 'secondary', 'primary', 'info', 'success', 'warning', 'error',
    'MessageFailure'
)


class MessageFailure(Exception):
    pass


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
        return backend.send_message(level, text, subject, extra, to_users_pk, to_groups_pk, True, html_safe,
                                    reply_to_pk)


def all(request: HttpRequest):  # noqa
    """
    Return all messages on the request if it exists, otherwise return an empty list.
    """
    try:
        return request.dmm_backend.all_messages
    except AttributeError:
        return []


def all_count(request: HttpRequest):
    """
    Return all messages count on the request if exist, otherwise return 0
    """
    try:
        return request.dmm_backend.all_messages_count
    except AttributeError:
        return 0


def read(request: HttpRequest):
    """
    Return read messages on the request if it exists, otherwise return an empty list.
    """
    try:
        return request.dmm_backend.read_messages
    except AttributeError:
        return []


def read_count(request: HttpRequest):
    """
    Return read messages count on the request if exist, otherwise return 0
    """
    try:
        return request.dmm_backend.read_messages_count
    except AttributeError:
        return 0


def unread(request: HttpRequest):
    """
    Return unread messages on the request if it exists, otherwise return an empty list.
    """
    try:
        return request.dmm_backend.unread_messages
    except AttributeError:
        return []


def unread_count(request: HttpRequest):
    """
    Return unread messages count on the request if exist, otherwise return 0
    """
    try:
        return request.dmm_backend.unread_messages_count
    except AttributeError:
        return 0


def archived(request: HttpRequest):
    """
    Return archived messages on the request if it exists, otherwise return an empty list.
    """
    try:
        return request.dmm_backend.archived_messages
    except AttributeError:
        return []


def archived_count(request: HttpRequest):
    """
    Return archived messages count on the request if exist, otherwise return 0
    """
    try:
        return request.dmm_backend.archived_messages_count
    except AttributeError:
        return 0


def new(request: HttpRequest):
    """
    Return new messages on the request if it exists, otherwise return an empty list.
    """
    try:
        return request.dmm_backend.new_messages
    except AttributeError:
        return []


def new_count(request: HttpRequest):
    """
    Return archived messages count on the request if exist, otherwise return 0
    """
    try:
        return request.dmm_backend.new_messages_count
    except AttributeError:
        return 0


def new_count_update_last_checked(request: HttpRequest):
    """
    Return archived messages count on the request if exist, otherwise return 0
    """
    try:
        return request.dmm_backend.new_messages_count
    except AttributeError:
        return 0


def secondary(request: HttpRequest,
              text: str = None,
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
