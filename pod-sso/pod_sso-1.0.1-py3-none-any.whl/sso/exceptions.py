from pod_base import PodException


class SSOException(PodException):
    __slots__ = ("error", "error_description", "status_code")

    def __init__(self, status_code, error, error_description):
        self.status_code = status_code
        self.error = error
        self.error_description = error_description
        super(SSOException, self).__init__(error_description)
