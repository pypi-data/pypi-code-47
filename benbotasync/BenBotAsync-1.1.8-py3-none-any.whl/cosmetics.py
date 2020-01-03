from .http import HTTPClient

class fortniteCosmetic:
    def __init__(self, data):
        for key,value in data.items():
            self.__setattr__(key, value)
