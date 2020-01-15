"""
Exceptions for the spec Validator
"""
from dataclasses import dataclass


__all__ = ["ValidationException", "YamlSchemaException", "Spec122ValidationException", "Spec214ValidationException"]


class ValidationException(Exception):
    """
    Base Exception for the validator
    """

@dataclass
class YamlSchemaException(ValidationException):
    """
    Exception when validating the YAML Schemas
    """

    def __str__(self):
        return f"Errors during Yaml Validation. Keyword:{self.key} Error:{self.errors}"

    def __repr__(self):
        return f"YamlSchemaException(errors={schemaerrors})"

    errors: dict = None
    key: str = None


@dataclass
class Spec122ValidationException(ValidationException):
    """
    Exception when validating a spec 122 file
    """

    def __str__(self):
        return f"Errors during Ingest Validation: {self.errors}"

    def __repr__(self):
        return f"Spec122ValidationException(errors={all_errors})"

    errors: dict = None

@dataclass
class Spec214ValidationException(ValidationException):
    """
    Exception when validating a spec 214 file
    """

    def __str__(self):
        return f"Errors during Ingest Validation: {self.errors}"

    def __repr__(self):
        return f"Spec214ValidationException(errors={all_errors})"

    errors: dict = None
