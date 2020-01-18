from .vkObject import VkObject


class Action(VkObject):
    def __init__(self, json):
        self.json = json
        self.type = self.json.get("type")
        self.member_id = self.json.get("member_id")
        self.text = self.json.get("text")
        self.email = self.json.get("email")
        self.photo = self.json.get("photo")
