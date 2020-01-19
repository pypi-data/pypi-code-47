"""
This module defines some custom model fields for Django.
"""
# import logging

# Use with logging (if settings.DEBUG: logger.debug(...))
# from django.conf import settings

from django.contrib.postgres.fields import JSONField

from polyquack.translation import Translatable

from .form_fields import TranslatablePgJSONFormField

# logger = logging.getLogger("django")


class TranslatablePgJSONField(JSONField):
    """
    This class offers a Translatable PostgreSQL JSONField.
    """

    description = "This class offers a Translatable PostgreSQL JSONField."

    def __init__(
        self, match_level: str = None, default_language: str = None, *args, **kwargs,
    ):
        self.match_level = match_level
        self.default_language = default_language
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.match_level is not None:
            kwargs["match_level"] = self.match_level
        if self.default_language is not None:
            kwargs["default_language"] = self.default_language
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return Translatable(
            translations=value,
            match_level=self.match_level,
            default=self.default_language,
        )

    def formfield(self, **kwargs):
        defaults = {"form_class": TranslatablePgJSONFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
