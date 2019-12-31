import threading
import time
from functools import wraps


def rate_limited(max_per_second):
    lock = threading.Lock()
    min_interval = 1.0 / max_per_second

    def decorate(func):
        last_time_called = time.perf_counter()

        @wraps(func)
        def rate_limited_function(*args, **kwargs):
            lock.acquire()
            nonlocal last_time_called
            elapsed = time.perf_counter() - last_time_called
            left_to_wait = min_interval - elapsed

            if left_to_wait > 0:
                time.sleep(left_to_wait)

            ret = func(*args, **kwargs)
            last_time_called = time.perf_counter()
            lock.release()
            return ret

        return rate_limited_function

    return decorate


class RateLimitedGroup:
    def __init__(self, max_per_second: float):
        self.max_per_second = max_per_second
        self.lock = threading.Lock()
        self.min_interval = 1.0 / max_per_second
        self.last_time_called = time.perf_counter()

    def __call__(self, func):
        @wraps(func)
        def rate_limited_function(*args, **kwargs):
            self.lock.acquire()
            elapsed = time.perf_counter() - self.last_time_called
            left_to_wait = self.min_interval - elapsed

            if left_to_wait > 0:
                time.sleep(left_to_wait)

            ret = func(*args, **kwargs)
            self.last_time_called = time.perf_counter()
            self.lock.release()
            return ret

        return rate_limited_function
