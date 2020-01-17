"""Support for multilingual strings in oarepo invenio repository."""

from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow.fields import List, Nested


class MultilingualStringPartSchemaV1(StrictKeysMixin):
    """Multilingual string."""

    value = SanitizedUnicode(required=True)
    lang = SanitizedUnicode(required=True)


def MultilingualStringSchemaV1(**kwargs):
    """Return a schema for multilingual string."""
    return Nested(MultilingualStringPartSchemaV1(many=True), many=True, **kwargs)


__all__ = ('MultilingualStringSchemaV1',)
