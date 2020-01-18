from gva.methods.methodAbs import MethodObject
from gva.requests import execute_method


METHOD = "groups.getById"


class getById(MethodObject):
    def __init__(self, api, **data):
        super().__init__()
        self.api = api
        self._execute(data)

    def _execute(self, data):
        self.raw_response = execute_method(self.api, METHOD, **data)

        self.id = self.raw_response.get("id")
        self.name = self.raw_response.get("name")
        self.screen_name = self.raw_response.get("screen_name")
        self.is_closed = self.raw_response.get("is_closed")
        self.deactivated = self.raw_response.get("deactivated")
        self.type = self.raw_response.get("type")
        self.photo_50 = self.raw_response.get("photo_50")
        self.photo_100 = self.raw_response.get("photo_100")
        self.photo_200 = self.raw_response.get("photo_200")
        self.activity = self.raw_response.get("activity")
        self.age_limits = self.raw_response.get("age_limits")
        self.ban_info = self.raw_response.get("ban_info")
        # Нужны то, что приходит, но я это не добави? Сделай сам!
        # [SPOILER] Или создай issue [/SPOILER]
