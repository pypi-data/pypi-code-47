from gva.methods.methodAbs import MethodObject
from gva.requests import execute_method

METHOD = "messages.delete"


class delete(MethodObject):
    __slots__ = {
        "api",
        "result"
    }

    def __init__(self, api, **data):
        super().__init__()
        self.api = api
        self._execute(data)

    def _execute(self, data):
        self.result = execute_method(self.api, METHOD, **data)
