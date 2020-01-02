"""
handler contains types of pre-defined handlers.
"""

from functools import wraps


def noop(_):
    """
    noop handler does nothing.
    """
    return None


def status(f):
    """
    status is a decorator function to return the response with the status code.
    """
    def status_func(code):
        @wraps(f)
        def decorated(request):
            resp = f(request)
            resp.status = code
            return resp
        return decorated
    return status_func


def file(f):
    """
    file is a decorator function to return content of the file.
    """
    def file_func(path):
        @wraps(f)
        def decorated(_):
            # TODO: read path and return the content
            return path
        return decorated
    return file_func
