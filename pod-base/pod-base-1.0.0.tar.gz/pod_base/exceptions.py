class PodException(Exception):
    __slots__ = "message"

    def __init__(self, message, *args, **kwargs):
        self.message = message
        super(Exception, self).__init__(*args)


class InvalidDataException(PodException):
    pass


class HTTPException(PodException):
    __slots__ = ("status_code", "raw_result")

    def __init__(self, *args, **kwargs):
        self.status_code = kwargs.pop('status_code', None)
        self.raw_result = kwargs.pop('raw_result', None)
        message = kwargs.pop('message', "")

        super(HTTPException, self).__init__(message, *args, **kwargs)


class APIException(PodException):
    __slots__ = ("message", "reference_number")

    def __init__(self, message, reference_number=None):
        if reference_number is None:
            reference_number = ""

        super(APIException, self).__init__(message)
        self.reference_number = reference_number


class ConfigException(PodException):
    pass


class ServiceCallException(PodException):
    pass
