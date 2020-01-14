"""
This module defines some custom fields for Django.
"""
from django.contrib.postgres.fields import JSONField


class TranslatablePgJSONField(JSONField):
    """
    This class offers a Translatable PostgreSQL JSONField.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

