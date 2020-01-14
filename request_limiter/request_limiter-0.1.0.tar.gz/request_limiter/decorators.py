import threading
from functools import wraps
from typing import Optional

from request_limiter.exceptions import LimitException
from request_limiter.strategy import LimitStrategy, LimitedIntervalStrategy


class RequestLimiterDecorator(object):
    """
    A decorator class used to limit request rate to a function using a custom strategy or the default
    LimitedIntervalStrategy.
    """
    def __init__(self, strategy: Optional[LimitStrategy] = None):
        """
        :param strategy: A request limit strategy
        """
        self.strategy = strategy or LimitedIntervalStrategy()

    def __call__(self, f):
        """
        Returns a wrapped function that checks the strategy before invoking the function
        :param f: The function to be wrapped
        :return: Wrapped function
        """
        # Run clean up daemon in background
        clean_task = threading.Thread(target=self.strategy.clean, daemon=True)
        clean_task.start()

        @wraps(f)
        def wrapper(*args, **kwargs):
            """
            Checks and raises LimitException if the function reached the maximum allowed invocation
            """
            with threading.RLock():  # Request in a tread safe way
                key = kwargs.pop('limit_key', None)
                if not self.strategy.request(key=key):  # Failed to allocate
                    raise LimitException('Rate limit exceeded.', self.strategy)

            return f(*args, **kwargs)
        return wrapper


def django_request_limiter(f):
    """
    Returns a wrapped function for django request handler function.
    It applies limit strategy based on request IP and returns 429.
    :param f: django request handler function decorated with request_limiter
    :return: wrapped function
    """
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        # Set the default limit per IP
        ip = request.META.get('REMOTE_ADDR')
        kwargs['limit_key'] = ip
        try:
            return f(request, *args, **kwargs)
        except LimitException as e:
            from django.http import HttpResponse
            body = "Rate limit exceeded. Try again in {} seconds".format(e.strategy.get_remaining(ip))
            return HttpResponse(body, status=429)
    return wrapper
