import json

from django.db import models

from django_magnificent_messages.fields import JSONField, JSONFieldConvertError


class JSONFieldDefaultModel(models.Model):
    field = JSONField(null=True)

    class Meta:
        db_table = "default"


class CustomClass:
    def __init__(self, num, string):
        self.num = num
        self.string = string

    def __eq__(self, other):
        return self.num == other.num and self.string == other.string


def custom_encode(val):
    try:
        d = {
            "num": val.num,
            "string": val.string,
        }

        return json.dumps(d, ensure_ascii=True)
    except TypeError:
        raise JSONFieldConvertError(
            val,
            message=_("Error while decoding value `%(value)r` in field `%(name)s"),
            code="encode_error"
        )


def custom_decode(json_string):
    try:
        d = json.loads(json_string)
        return CustomClass(**d)
    except (TypeError, json.decoder.JSONDecodeError):
        raise JSONFieldConvertError(
            json_string,
            message=_("Error while decoding value `%(value)r` in field `%(name)s"),
            code="encode_error"
        )


class JSONFieldCustomModel(models.Model):
    field = JSONField(encode=custom_encode, decode=custom_decode)

    class Meta:
        db_table = "custom"
