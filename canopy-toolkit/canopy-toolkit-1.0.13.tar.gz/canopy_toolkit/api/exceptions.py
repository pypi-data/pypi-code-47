from typing import List

from requests import Response


class MultiValueException(Exception):
    """An Exception that can have multiple error values."""

    errors: List[str] = []

    def __init__(self, message, errors: List[str] = None):
        """
        Initialize an exception instance containing multiple errors.

        :param message: the message to add
        :param errors: the errors
        """
        if errors is None:
            self.errors.append(message)
        else:
            self.errors = errors


class CanopyClientException(MultiValueException):
    """Exception thrown when an API Client Operation fails."""

    pass


class MultiFactorAuthenticationRequired(CanopyClientException):
    """Exception thrown when MFA is required to login."""

    pass


class MultiFactorActivationRequired(CanopyClientException):
    """Exception thrown when MFA activation is required to login."""

    pass


class CanopyAPIException(CanopyClientException):
    """Exception thrown when an API call fails."""

    errors: List[str]
    status_code: int

    def __init__(self, message, response: Response = None):
        """
        Initialize an exception instance and parse the response body into errors array.

        :param message: the message to add
        :param response: the raw response from requests
        """
        super().__init__(message)
        self.message = message
        self.errors = []

        if response is not None:
            self.status_code = response.status_code
            try:
                body = response.json()
                if body is not None:
                    for key in ['error', 'errors', 'messages', 'errorMessages']:
                        if key in body:
                            error = body[key]
                            if isinstance(error, list):
                                self.errors = self.errors + error
                            else:
                                self.errors.append(error)
            except Exception:
                self.errors.append(response.text)
        else:
            self.errors = [message]
