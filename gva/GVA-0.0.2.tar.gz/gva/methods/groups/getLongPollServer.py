from gva.methods.methodAbs import MethodObject
from gva.requests import execute_method

METHOD = "groups.getLongPollServer"


class getLongPollServer(MethodObject):
    def __init__(self, api, **data):
        super().__init__()
        self.api = api
        self._execute(data)

    def _execute(self, data):
        self.raw_response = execute_method(self.api, METHOD, **data)
        self.key = self.raw_response.get("key")
        self.ts = self.raw_response.get("ts")
        self.server = self.raw_response.get("server")
        self.failed = self.raw_response.get("failed")
