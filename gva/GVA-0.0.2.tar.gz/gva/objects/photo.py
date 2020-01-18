from .vkObject import VkObject


class Photo(VkObject):
    def __init__(self, json):
        self.json = json
        self.id = self.json.get("id")
        self.album_id = self.json.get("album_id")
        self.owner_id = self.json.get("owner_id")
        self.user_id = self.json.get("user_id")
        self.text = self.json.get("text")
        self.date = self.json.get("date")
        self.sizes = Photo.get_sizes(self.json.get("sizes"))

    @staticmethod
    def get_sizes(sizes):
        return {size.type: size for size in [PhotoSize(x) for x in sizes]}


class PhotoSize(VkObject):
    def __init__(self, json):
        self.json = json
        self.src = self.json.get("src")
        self.width = self.json.get("width")
        self.height = self.json.get("height")
        self.type = self.json.get("type")
