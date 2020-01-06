import functools


class FailedOperation(Exception):
    """Represents an exception that was caused by a failure
    of a requested operation.
    """
    default_status = 421
    default_code = 'UNKNOWN_ERROR'

    @classmethod
    def catch(cls, on_exception):
        """Returns a decorator that invokes callable `on_exception`
        when a :class:`FailedOperation` is raised.
        """
        def decorator(func):
            @functools.wraps(func)
            def f(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except FailedOperation as e:
                    return on_exception(e)
            return f
        return decorator

    def __init__(self, status=None, code=None, stderr=None):
        self.code = code or self.default_code
        self.status = status or self.default_status
        self.stderr = stderr or ''

    @property
    def dto(self):
        return {
            'code': self.code,
            'stderr': self.stderr
        }


class AccessDenied(FailedOperation):
    """Raised when an operation fails due to request not
    having permission.
    """
    default_code = 'ACCESS_DENIED'
    default_status = 401


class ResourceDoesNotExist(FailedOperation):
    """Raised when an operation fails due to an upstream
    resource not existing.
    """
    default_code = 'DOES_NOT_EXIST'
    default_status = 404


class Unreachable(FailedOperation):
    """Raised when an operation fails due to an upstream
    resource not being reachable.
    """
    default_code = 'UNREACHABLE'
    default_status = 503


class Timeout(Unreachable):
    """Raised when an operation fails due to a timeout
    when accessing an upstream resource.
    """
    pass
