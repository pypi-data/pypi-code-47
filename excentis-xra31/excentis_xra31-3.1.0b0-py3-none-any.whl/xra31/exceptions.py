"""Exceptions specific to the XRA-31."""


class Xra31Warning(Warning):
    """Warning for XRA-31."""


class Xra31Exception(Exception):
    """Raised in case of an XRA-31 related exception."""


class Xra31RestException(Xra31Exception):
    """Raised in case of a REST Exception."""


class Xra31RestWarning(Xra31Warning):
    """Raised in case of a REST Warning."""


class Xra31ConnectionException(Xra31RestException):
    """Raised in case of a REST Connection Exception."""


class Xra31HttpException(Xra31RestException):
    """Raised in case of a REST HTTP Exception."""


class Xra31ClientException(Xra31HttpException):
    """Raised in case of a REST HTTP Client Exception."""


class Xra31ServerException(Xra31HttpException):
    """Raised in case of a REST HTTP Server Exception."""


class Xra31StateException(Xra31Exception):
    """Raised in case an action is incompatible with the current state."""


class Xra31FullAccessException(Xra31Exception):
    """Raised in case full-access mode is required."""


class Xra31TimeoutException(Xra31Exception):
    """Raised in case a timeout occurred."""


class Xra31ConfigurationException(Xra31Exception):
    """Raised in case of an inconsistent configuration for the XRA-31."""


class Xra31FileNotFoundException(Xra31Exception):
    """Raised in case a file can not be found on the XRA-31."""
