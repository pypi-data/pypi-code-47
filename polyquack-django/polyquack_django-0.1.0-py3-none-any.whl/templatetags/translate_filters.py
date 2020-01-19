"""
Django template filters.
"""

from django import template

register = template.Library()


@register.filter(name="get_translation")
def get_translation(translatable, language):
    """
    Usage:
        {% load translate_filters %}
        {{ translatable_instance | get_translation: "en-ca" }}
    """
    return translatable.translate(language)
