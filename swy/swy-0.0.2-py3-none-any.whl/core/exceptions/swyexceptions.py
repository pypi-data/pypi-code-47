"""
Exceptions for the SWY app


SwyException
    - AdbException
        - PhoneNotFoundException
        - MultiplePhonesException
        - PhoneLibNotFoundException


SwyWarning
    - AdbWarning
        - CompatibilityPhoneSelectedWarning

"""


class SwyException(Exception):
    """
    Root exception for the app
    """


class AdbException(SwyException):
    """
    Root exception for the ADB service
    """


class PhoneNotFoundException(AdbException):
    """
    The phone to interact with has not been found
    """


class MultiplePhonesException(AdbException):
    """
    Currently, there is no intent and need to support multiples phones at
    the same time.
    """


class PhoneLibNotFoundException(AdbException):
    """
    When no module has been found for the current phone
    """


class SwyWarning(Warning):
    """
    Root warning for the app
    """


class CompatibilityPhoneSelectedWarning(SwyWarning):
    """
    The phone module has been selected according to an untested compatibility,
    and may have a strange comportment.
    """
