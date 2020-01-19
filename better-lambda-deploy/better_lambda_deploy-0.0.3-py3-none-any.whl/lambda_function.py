from abc import ABC
import sys


class LambdaFunction(ABC):
    def _init_(self, event, context):
        print("Lambda init.")
        print(event)

    def __call__(self, event, context):
        self.__init__()

        response = self.run(event, context)

        return response

    @classmethod
    def get_handler(cls, *args, **kwargs):
        def handler(event, context):
            return cls(*args, **kwargs).handle(event, context)

        return handler

    def run(self, event, context):
        raise NotImplementedError


def LambdaHandler(func):
    # Creates dynamic handler in caller's module called MyCallingClassHandler

    module = func.__module__
    handler_name = f"{func.__name__}Handler"
    setattr(sys.modules[module], handler_name, func.get_handler())
    return func
