# -*- coding: utf-8 -*-
from django import template
from django.utils import translation

# from common.utils.common import add_slash_right

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def str_in_list(value, arg):
    try:
        return str(value) in arg
    except (ValueError, ZeroDivisionError):
        return False
