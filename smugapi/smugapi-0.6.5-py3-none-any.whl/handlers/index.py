
from .base import BaseHandler, route


@route('/?')
class IndexHandler(BaseHandler):

    def get(self):
        self.write("smugapi")


