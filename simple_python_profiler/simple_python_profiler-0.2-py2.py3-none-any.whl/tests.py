from random import random

from simple_python_profiler.main import Profiler, profile_recursive


def sub():
    print('in sub')

    @profile_recursive
    def inner():
        print('in inner')

        def inner2():
            print('in inner2')

        inner2()

    inner()

    return random()


# @profile
def go(a, b):
    print('in go')

    # @profile
    def inner():
        print('in inner2')

    sub()
    inner()
    return random()


if __name__ == '__main__':
    with Profiler():
        go(1, 2)
        sub()
        # go(1, 2)
