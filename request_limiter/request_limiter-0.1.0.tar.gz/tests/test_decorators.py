import os
import unittest
from typing import Optional

from django.http import HttpResponse
from django.test import RequestFactory

from request_limiter import request_limiter, LimitedIntervalStrategy, \
    LimitStrategy, LimitException, django_request_limiter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')
req_factory = RequestFactory()


class MockStrategy(LimitStrategy):
    def __init__(self, allow: bool):
        self.allow = allow

    def request(self, key: Optional[str] = None) -> bool:
        return self.allow

    def get_remaining(self, key: Optional[str] = None) -> float:
        return 1

    def clean(self):
        pass


class TestRequestLimiterDecorator(unittest.TestCase):

    def test_when_strategy_not_given_uses_limited_interval_strategy(self):
        limiter = request_limiter()
        self.assertTrue(isinstance(limiter.strategy, LimitedIntervalStrategy))

    def test_when_strategy_allows_invokes_function(self):
        @request_limiter(strategy=MockStrategy(allow=True))
        def test_func() -> bool:
            return True

        self.assertTrue(test_func())

    def test_when_strategy_denies_raises_exception(self):
        @request_limiter(strategy=MockStrategy(allow=False))
        def test_func() -> bool:
            return True

        self.assertRaises(LimitException, test_func)


class TestDjangoRequestLimiter(unittest.TestCase):

    def test_limits_based_on_ip(self):
        @django_request_limiter
        @request_limiter(strategy=LimitedIntervalStrategy(requests=1))
        def test_view(request):
            return True

        res1 = test_view(req_factory.post('/test/', REMOTE_ADDR='127.0.0.1'))
        assert res1, 'Expected first request to work'

        res2 = test_view(req_factory.post('/test/', REMOTE_ADDR='127.0.0.1'))
        assert isinstance(res2, HttpResponse), 'Expected limit http response'
        assert res2.status_code == 429, 'Expected 429 response code'

        # change Ip
        res3 = test_view(req_factory.post('/test/', REMOTE_ADDR='127.0.0.2'))
        assert res3, 'Expected different ip request to work'
