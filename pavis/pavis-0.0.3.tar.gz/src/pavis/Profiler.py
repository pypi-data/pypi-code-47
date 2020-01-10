from functools import wraps
import time

def func_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, 'took', end - start, 'seconds')
        return result
    return wrapper

@func_time
def test():
    for x in range(10000):
        print(x)

if __name__ == "__main__":
    test()