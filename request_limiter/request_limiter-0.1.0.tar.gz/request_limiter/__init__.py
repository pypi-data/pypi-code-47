"""Top-level package for Request Limiter."""
from request_limiter.decorators import RequestLimiterDecorator, django_request_limiter
from request_limiter.exceptions import LimitException
from request_limiter.strategy import LimitStrategy, LimitedIntervalStrategy

__author__ = """Mati Bekuma Terefe"""
__email__ = 'matibek@gmail.com'
__version__ = '0.1.0'

request_limiter = RequestLimiterDecorator

__all__ = [
    'request_limiter',
    'django_request_limiter',
    'LimitStrategy',
    'LimitedIntervalStrategy',
    'LimitException'
]
