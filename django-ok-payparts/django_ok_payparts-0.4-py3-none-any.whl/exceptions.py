__all__ = (
    'PayPartsException',
    'InvalidAuthDataError',
    'InvalidTokenError'
)


class PayPartsException(AttributeError):
    pass


class InvalidAuthDataError(PayPartsException):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class InvalidTokenError(InvalidAuthDataError):
    pass
