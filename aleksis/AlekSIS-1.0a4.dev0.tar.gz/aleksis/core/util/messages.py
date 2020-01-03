import logging
from typing import Any, Optional

from django.contrib import messages
from django.http import HttpRequest


def add_message(
    request: Optional[HttpRequest], level: int, message: str, **kwargs
) -> Optional[Any]:
    if request:
        return messages.add_message(request, level, message, **kwargs)
    else:
        return logging.getLogger(__name__).log(level, message)


def debug(request: Optional[HttpRequest], message: str, **kwargs) -> Optional[Any]:
    return add_message(request, messages.DEBUG, message, **kwargs)


def info(request: Optional[HttpRequest], message: str, **kwargs) -> Optional[Any]:
    return add_message(request, messages.INFO, message, **kwargs)


def success(request: Optional[HttpRequest], message: str, **kwargs) -> Optional[Any]:
    return add_message(request, messages.SUCCESS, message, **kwargs)


def warning(request: Optional[HttpRequest], message: str, **kwargs) -> Optional[Any]:
    return add_message(request, messages.WARNING, message, **kwargs)


def error(request: Optional[HttpRequest], message: str, **kwargs) -> Optional[Any]:
    return add_message(request, messages.ERROR, message, **kwargs)
