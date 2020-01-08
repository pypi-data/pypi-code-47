"""
This contains various tools for testing and optimizing
"""
import time
from functools import wraps


def timefn(fn):
    """
    Decorator to time operation of method
    From High Performance Python, p.27
    """
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        elapsed = str(t2 - t1)
        print(("@timefn:%s took %s seconds" % (fn.__name__, elapsed)))
        #         print(("@timefn:%s took %s seconds" % (fn.__name__, elapsed)))
        return result
    return measure_time


class Timer(object):
    def __init__(self):
        self.elapsed_seconds = 0
        self.start_time = None

    def start(self, reset=True):
        """Starts the timer
        reset: Whether to start the timer f"""
        if reset is True: self.elapsed_seconds = 0
        self.start_time = time.time()

    def _calc_elapsed(self):
        self.elapsed_seconds += time.time( ) - self.start_time

    def stop(self):
        """Stops the timer"""
        self._calc_elapsed()
        print ("Execution took %s seconds" % self.elapsed_seconds)
