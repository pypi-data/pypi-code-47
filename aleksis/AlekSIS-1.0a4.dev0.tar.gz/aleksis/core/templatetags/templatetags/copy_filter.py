import copy as copylib

from django import template

register = template.Library()

register.filter("copy", copylib.copy)
register.filter("deepcopy", copylib.deepcopy)
