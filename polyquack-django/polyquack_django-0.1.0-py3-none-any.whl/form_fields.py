import json

from django.contrib.postgres.forms import JSONField

from polyquack.translation import Translatable


class TranslatablePgJSONFormField(JSONField):
    def prepare_value(self, value):
        # Return translations when we have a Translatable object
        if isinstance(value, Translatable):
            return json.dumps(value.translations)
        # When creating a new instance, we start with an empty dict, so return just that
        return value
