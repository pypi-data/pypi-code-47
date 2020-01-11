__all__ = (
    'ESputnikException',
    'InvalidAuthDataError',
    'IncorrectDataError'
)


class ESputnikException(AttributeError):
    pass


class InvalidAuthDataError(ESputnikException):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class IncorrectDataError(InvalidAuthDataError):
    pass
