from ..completer import Completer as CompleterClass
from ..completer import CompleterStyle
from ..loader import LoaderStyle, Loader as LoaderClass


class Completer:
    def __init__(self, message, style=CompleterStyle()):
        self.message = message
        self.ctype = style

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            c = CompleterClass(self.message, self.ctype).init()
            try:
                r = func(*args, **kwargs)
            except Exception as e:
                c.fail(e)
                raise e

            c.complete()
            return r

        return wrapper


class Loader:
    def __init__(self, message, style=LoaderStyle(5)):
        self.message = message
        self.style = style

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            l = LoaderClass(message=self.message, style=self.style).init()
            try:
                r = func(*args, **kwargs)
            except Exception as e:
                l.fail(e)
                raise e

            l.complete()

            return r

        return wrapper
