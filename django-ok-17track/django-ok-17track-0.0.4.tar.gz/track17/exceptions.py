"""
Define custom exceptions
"""

__all__ = (
    'Track17Exception',
    'InvalidCarrierCode',
    'DateProcessingError'
)


class Track17Exception(Exception):
    def __init__(self, message: str, code: int = None):
        self.message = message
        self.code = code
        super().__init__()

    def __str__(self) -> str:
        if self.code:
            return f'{self.message} (Code: {self.code})'
        return self.message


class InvalidCarrierCode(Track17Exception):
    pass


class DateProcessingError(Track17Exception):
    pass
