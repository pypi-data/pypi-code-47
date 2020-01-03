# -*- coding: utf-8 -*- 
# @Time     : 2019-12-25 17:00
# @Author   : binger

import time
import sys
import logging

logger = logging.getLogger("utils")


def new_registry(attribute=None):
    """
    Returns an empty dict and a @register decorator.
    """
    registry = {}

    def register(key: str):
        def decorator(func):
            registry[key] = func
            if attribute:
                setattr(func, attribute, key)
            return func

        return decorator

    return registry, register


from functools import wraps


# 3s 执行， 默认重复3次吗， 有唤醒，先唤醒，没唤醒不执行
def apply_repeat_run(awake_cb=None, at_exception_cb=None, tries=3, interval=0.1, timeout=3):
    """add apply_connect_continued semantics to a function."""

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            n = 0
            exception_stack = None
            start = time.time()
            while n != tries:
                if n != 0 and awake_cb and not awake_cb():
                    continue
                else:
                    n += 1
                    try:
                        result = func(*args, **kwargs)
                        break
                    except Exception as e:
                        exception_stack = e
                        if at_exception_cb and at_exception_cb(e):
                            if time.time() - start > timeout:
                                raise e
                            time.sleep(interval)
                        else:
                            raise e
            else:
                raise exception_stack
            logger.debug("takes: {}, user NO.:{}".format(round(time.time() - start, 2), n))
            return result

        # decorator.__name__ = func.__name__
        return wrapper

    # apply_repeat_run.__name__ = decorator.__name__

    # print("decorator: ", decorator)
    return decorator


if __name__ == "__main__":
    pass
