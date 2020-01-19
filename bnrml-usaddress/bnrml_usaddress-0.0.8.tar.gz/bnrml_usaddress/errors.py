#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 6/29/19
"""
.. currentmodule:: bnrml_usaddress.errors
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Sometimes things go wrong.
"""


class BnrmlUsAddressException(Exception):
    """Base exception for other exceptions defined in this library."""
    def __init__(self, message: str, inner: Exception = None):
        """

        :param message: the exception message
        :param inner: the exception that caused this exception
        """
        super().__init__(message)
        self._message = message
        self._inner = inner

    @property
    def message(self) -> str:
        """
        Get the exception message.
        """
        return self._message

    @property
    def inner(self) -> Exception or None:
        """
        Get the exception that caused this exception.
        """
        return self._inner


class BnrmlUsAddressValueError(BnrmlUsAddressException):
    """The value is unrecognized, cannot be parsed, or is otherwise bad."""
