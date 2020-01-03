# -*- coding: utf-8 -*- 
# @Time     : 2020-01-02 18:41
# @Author   : binger

import json


class Response(object):
    __slots__ = ['code', 'message', 'data', 'original_exception']

    def __init__(self, code=0, message=None, data=None):
        self.code = code
        self.message = message
        self.data = data
        self.original_exception = None

    def to_dict(self):
        if self.code:
            return dict(code=self.code, message=self.message)
        else:
            return dict(code=self.code, data=self.data)

    @property
    def json(self):
        return json.dumps(self.to_dict())


if __name__ == "__main__":
    pass
