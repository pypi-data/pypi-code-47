from inspect import signature

def f():
    return 10

def g(a: int) -> int:
    return a + 10

def h(a: int, *arg) -> int:
    return a + 10
