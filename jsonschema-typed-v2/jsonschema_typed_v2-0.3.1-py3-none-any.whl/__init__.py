"""This space intentionally left blank."""


class JSONSchema(dict):
    """Placeholder for JSON schema TypedDict."""

    def __class_getitem__(cls, item):
        return dict
