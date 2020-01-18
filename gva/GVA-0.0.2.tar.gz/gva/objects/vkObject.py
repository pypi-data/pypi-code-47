import json


class VkObject:
    __slots__ = {"json"}

    def __str__(self):
        return json.dumps(self.json, indent=4, ensure_ascii=False)

    @staticmethod
    def __new__(cls, vk_object):
        if vk_object is None:
            return None
        else:
            return object.__new__(cls)
