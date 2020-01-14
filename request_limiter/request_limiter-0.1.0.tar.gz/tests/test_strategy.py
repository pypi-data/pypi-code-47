import threading
import time
import unittest

from request_limiter import LimitedIntervalStrategy


class NowMocker(object):
    def __init__(self):
        self.seconds = 0

    def __call__(self):
        return self.seconds


class TestLimitedIntervalStrategy(unittest.TestCase):
    def setUp(self):
        self.now = NowMocker()

    def test_default_request_limit_and_period(self):
        stg = LimitedIntervalStrategy(now=self.now)
        self.assertEqual(stg.requests, 100)
        self.assertEqual(stg.interval, 24 * 60 * 60)
        self.assertEqual(stg.storage, {})

    def test_when_request_is_allowed_it_increase_request_count(self):
        storage = {}
        stg = LimitedIntervalStrategy(now=self.now, storage=storage)
        assert stg.request(), 'Expected to allow request'
        self.assertEqual(storage[stg.DEFAULT_KEY]['request_count'], 1)

    def test_when_request_count_pass_limit_blocks_request(self):
        stg = LimitedIntervalStrategy(requests=1, interval=10, now=self.now)
        assert stg.request(), 'Expected first request to work'
        assert not stg.request(), 'Expected second request to fail'

    def test_when_interval_pass_reset_request_count(self):
        storage = {}
        stg = LimitedIntervalStrategy(requests=1, interval=10, now=self.now, storage=storage)
        stg.request()
        self.now.seconds = 11

        assert stg.request(), 'Expected request to work'
        self.assertEqual(storage[stg.DEFAULT_KEY]['request_count'], 1)

    def test_remaining_time(self):
        stg = LimitedIntervalStrategy(requests=1, interval=10, now=self.now)
        stg.request()
        self.now.seconds = 4

        self.assertEqual(stg.get_remaining(), 6)

    def test_clean_removes_expired_keys(self):
        self.now.seconds = 2
        storage = {'expired_key': {'reset_time': 0}, 'active_key': {'reset_time': self.now()}}
        stg = LimitedIntervalStrategy(requests=1, interval=1, now=self.now, storage=storage)
        task = threading.Thread(target=stg.clean, daemon=True)
        task.start()
        time.sleep(1)  # timeout for clean task

        assert 'expired_key' not in storage, 'Expected to remove expired key'
        assert 'active_key' in storage, 'Expected to keep active key'
