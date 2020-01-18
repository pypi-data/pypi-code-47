from .action import Action
from .attachments import Attachments
from .vkObject import VkObject


class Message(VkObject):
    def __init__(self, json):
        self.json = json
        self.id = self.json.get("id")
        self.date = self.json.get("date")
        self.peer_id = self.json.get("peer_id")
        self.from_id = self.json.get("from_id")
        self.text = self.json.get("text")
        self.random_id = self.json.get("random_id")
        self.ref = self.json.get("ref")
        self.ref_source = self.json.get("ref_source")
        self.raw_attachments = Attachments(self.json.get("attachments"))
        self.attachments = self.raw_attachments.array
        self.important = self.json.get("important")
        self.geo = self.json.get("geo")
        self.payload = self.json.get("payload")
        self.fwd_messages = self.json.get("fwd_messages")
        if self.fwd_messages is not None:
            self.fwd_messages = [Message(m) for m in self.json.get("fwd_messages")]
        self.reply_message = Message(self.json.get("reply_message"))
        self.action = Action(self.json.get("action"))
