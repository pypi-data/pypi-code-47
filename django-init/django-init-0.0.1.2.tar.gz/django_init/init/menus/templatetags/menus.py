# -*- coding: utf-8 -*-
from django import template
from common.menus.models import *

register = template.Library()


@register.simple_tag
def get_menu(key):
    return MenuItem.get_items(key)
