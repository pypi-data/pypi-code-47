# -*- coding: utf-8 -*-
"""
Django filters, needed when creating LaTeX files with the django template language

Written by Rocco Schulz (http://is-gr8.com/), modified by SchoolApps-Team
"""
from django.template.defaultfilters import stringfilter, register
from django.template.loader import render_to_string


@register.filter
@stringfilter
def brackets(value):
    """
    surrounds the value with { }
    You have to use this filter whenever you would need something like
    {{{ field }}} in a template.
    """
    return "{%s}" % value


REPLACEMENTS = {
    "§": "\\textsection{}",
    "$": "\\textdollar{}",
    "LaTeX": "\\LaTeX \\ ",
    " TeX": " \\TeX \\ ",
    "€": "\\euro",
    ">": "$>$",
    "<": "$<$"
}

ESCAPES = ("&", "{", "}", "%")


@register.filter
@stringfilter
def texify(value):
    """
    escapes/replaces special character with appropriate latex commands
    """
    tex_value = []

    # escape special symbols
    for char in value:
        tex_value.append("%s" % ("\\%s" % char if char in ESCAPES else char))
    tex_value = "".join(tex_value)

    # replace symbols / words with latex commands
    for key, value in REPLACEMENTS.items():
        tex_value = tex_value.replace(key, value)

    return "%s" % tex_value
