"""
Custom fields for django-magnificent-messages
"""
import json

from django.core import checks
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class JSONFieldConvertError(Exception):
    """
    Wrapper for all convert error.

    Should be used in encode/decode functions. Has three attributes:
      * text - text to be passed to ValidationError. You can use format syntax and following substitutions
        - {name} - field name
        - {verbose_name} - field verbose name
        - {value} - value which was passed as arg
      * value - value which was passed as arg
      * code - code of error
    """
    def __init__(self, value: object, message: str, code: str = 'convert_error'):
        super(JSONFieldConvertError, self).__init__()
        self.message = message
        self.value = value
        self.code = code


class JSONField(models.TextField):
    """
    JSON object field.

    Basically it's a TextField and you mostly can use it as such. But it takes two additional parameters `encode` and `
    decode` which should be callable of following signature:
      * encode(value: object) -> str
      * decode(json: str) -> object

    This functions used to convert python object to and from JSON-string. If something went wrong during
    encoding/decoding function should raise JSONFieldConvertError

    By default it's just use python standard json.loads and json.dumps with all of it's limitations. Check the docs.
    """
    description = _("String storing JSON-objects")

    def _raise_convert_validation_error(self, err: JSONFieldConvertError):
        raise ValidationError(
            err.message,
            code=err.code,
            params={
                "name": self.name,
                "verbose_name": self.verbose_name,
                "value": err.value
            }
        )

    @staticmethod
    def _default_encode(value: object) -> str:
        try:
            return json.dumps(value, ensure_ascii=False, sort_keys=True)
        except TypeError:
            raise JSONFieldConvertError(
                value,
                message=_("Error while decoding value `%(value)r` in field `%(name)s`"),
                code="encode_error"
            )

    @staticmethod
    def _default_decode(json_string: str) -> object:
        try:
            return json.loads(json_string)
        except (TypeError, json.decoder.JSONDecodeError):
            raise JSONFieldConvertError(
                json_string,
                message=_("Error while decoding value `%(value)r` in field `%(name)s"),
                code="encode_error"
            )

    def __init__(self, encode=None, decode=None, **kwargs):
        super(JSONField, self).__init__(**kwargs)
        self.encode = encode if encode is not None else self._default_encode
        self.decode = decode if decode is not None else self._default_decode
        self._encode_parameter = encode  # Saving for deconstruct
        self._decode_parameter = decode  # Saving for deconstruct

    def check(self, **kwargs):
        errors = super(JSONField, self).check(**kwargs)
        return errors + self._check_encode(**kwargs) + self._check_decode(**kwargs)

    def _check_encode(self, **_):
        if not callable(self.encode):
            return [
                checks.Error(
                    "Parameter `encode` of `JSONField` should be callable",
                    obj=self,
                    id='django_magnificent_messages.E101',
                )
            ]
        return []

    def _check_decode(self, **_):
        if not callable(self.decode):
            return [
                checks.Error(
                    "Parameter `decode` of `JSONField` should be callable",
                    obj=self,
                    id='django_magnificent_messages.E102',
                )
            ]
        return []

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self._encode_parameter is not None:
            kwargs['encode'] = self._encode_parameter
        if self._decode_parameter is not None:
            kwargs['decode'] = self._decode_parameter
        return name, path, args, kwargs

    def from_db_value(self, value, *_):
        if value is None:
            return value
        try:
            return self.decode(value)
        except JSONFieldConvertError as err:
            self._raise_convert_validation_error(err)

    def to_python(self, value):
        if isinstance(value, str) and value:
            try:
                return self.decode(value)
            except JSONFieldConvertError as err:
                self._raise_convert_validation_error(err)
        return value

    def get_prep_value(self, value):
        try:
            return self.encode(value)
        except JSONFieldConvertError as err:
            self._raise_convert_validation_error(err)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)
