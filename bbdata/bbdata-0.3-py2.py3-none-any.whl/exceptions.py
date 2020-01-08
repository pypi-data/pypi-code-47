"""BBData Exception Classes

Includes four exceptions: :class:

`.ResourceUnchangedException`, `.ResourceException`, `.UnknownResponseException` when something is
wrong on the server side. And if something happend on the client side, there is `.ClientException`.

If you need to create a new exception, extend the base class `.BBDataException`.
"""


class BBDataException(Exception):
    """The base BBData Exception that all other exception classes extend."""


class ResourceUnchangedException(BBDataException):
    """Exception raised when a query didn't modify the resource

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class ResourceException(BBDataException):
    """Exception raised when a resource:
         - isn't found
         - you don't have access to it
         - the request is malformed

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class UnknownResponseException(BBDataException):
    """Exception raised when the response to an API call is unknown

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message


class UnauthorizedException(BBDataException):
    """Exception raised when the user requests a resource he doesn't have access to.

    Attributes:
         message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message


class LoginRequiredException(BBDataException):
    """Exception raised when the user requests a resource he doesn't have access to.

    Attributes:
         message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message


class ClientException(BBDataException):
    """Exception raised that don't involve interaction with BBData's API.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

