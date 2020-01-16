from random import random


from simple_test_generator import Recorder


def sub():
    print('in sub')

    def inner():
        print('in inner')

        def inner2():
            print('in inner2')

        inner2()

    inner()

    from datetime import datetime

    return datetime(1970, 1, 1)


def return1():
    return 1


def go(a, b):
    print('in go')

    # @profile
    def inner():
        print('in inner2')

    sub()
    inner()
    return random()


def start():
    go(1, 2)
    sub()
    another.go(2, 3)


if __name__ == '__main__':
    with Recorder():
        start()
        # go(1, 2) #
    # Recorder().exit()
