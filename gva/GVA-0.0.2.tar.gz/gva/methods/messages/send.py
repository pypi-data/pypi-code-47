from gva.methods.methodAbs import MethodObject
from gva.requests import execute_method
from gva.utils import get_random_id

METHOD = "messages.send"


class send(MethodObject):
    __slots__ = {
        "peer_id",
        "message_id",
        "api",
        "raw_response"
    }

    def __init__(self, api, **data):
        super().__init__()
        self.api = api
        self._execute(data)

    def _execute(self, data):
        data["random_id"] = get_random_id()
        self.raw_response = execute_method(self.api, METHOD, **data)
        if isinstance(self.raw_response, dict):
            self.peer_id = self.raw_response.get("peer_id")
            self.message_id = self.raw_response.get("message_id")

        else:
            self.message_id = self.raw_response
