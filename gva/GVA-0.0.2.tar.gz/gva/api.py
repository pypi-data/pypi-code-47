from .methods.groups.getById import getById


class Api:
    def __init__(self, group_token, v=5.103):
        self.const = dict(access_token=group_token, v=v)
        self.const["group_id"] = getById(self)["id"]
