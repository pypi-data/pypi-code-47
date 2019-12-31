#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 12/27/19
"""
String utility methods.

.. currentmodule:: bnrml_usaddress.strutils
.. moduleauthor:: Pat Daburu <pat@daburu.net>
"""
import re


def camel_snake(camel: str) -> str:
    """
    Convert a camel-cased string to snake-case.

    :param camel: the camel-cased string
    :return: the snake-cased string
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def camel_dash(camel: str) -> str:
    """
    Convert a camel-cased string to dash-case.

    :param camel: the camel-cased string
    :return: the snake-cased string
    """
    _camel_snake = camel_snake(camel)
    return _camel_snake.replace('_', '-')
