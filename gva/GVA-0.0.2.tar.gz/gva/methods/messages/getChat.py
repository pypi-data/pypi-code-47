from gva.methods.methodAbs import MethodObject
from gva.requests import execute_method

METHOD = "messages.getChat"


class getChat(MethodObject):
    __slots__ = {
        "api",
        "raw_response",
        "id",
        "type",
        "title",
        "admin_id",
        "users",
        "push_settings",
        "photo_50",
        "photo_100",
        "photo_200",
        "left",
        "kicked"
    }

    def __init__(self, api, **data):
        super().__init__()
        self.api = api
        self._execute(data)

    def _execute(self, data):
        self.raw_response = execute_method(self.api, METHOD, **data)

        self.id = self.raw_response.get("id")
        self.type = self.raw_response.get("type")
        self.title = self.raw_response.get("title")
        self.admin_id = self.raw_response.get("admin_id")
        self.users = self.raw_response.get("users")
        self.push_settings = self.raw_response.get("push_settings")
        self.photo_50 = self.raw_response.get("photo_50")
        self.photo_100 = self.raw_response.get("photo_100")
        self.photo_200 = self.raw_response.get("photo_200")
        self.left = self.raw_response.get("left")
        self.kicked = self.raw_response.get("kicked")
