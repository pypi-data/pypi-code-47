from .vkObject import VkObject
from .photo import Photo


class Attachments(VkObject):
    def __init__(self, json):
        self.json = json
        class_of_vk_oject = {"photo": Photo,
                             "video": VkObject,
                             "audio": VkObject,
                             "doc": VkObject,
                             "link": VkObject,
                             "market": VkObject,
                             "market_album": VkObject,
                             "wall": VkObject,
                             "wall_reply": VkObject,
                             "sticker": VkObject,
                             "gift": VkObject,
                             "audio_message": VkObject,
                             "graffiti": VkObject
                             }
        self.array = [class_of_vk_oject[a["type"]](a[a["type"]]) for a in json]
