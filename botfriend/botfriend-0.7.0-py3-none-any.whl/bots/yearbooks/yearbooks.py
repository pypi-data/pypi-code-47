from pdb import set_trace
import json
import os
import random
import requests

from .ia import Text

class Yearbook(object):

    def __init__(self):
        self.identifier = None
        d = os.path.split(__file__)[0]
        self.by_year = json.load(
            open(os.path.join(d, "data", "yearbooks_by_year.json"))
        )
        while not self.identifier:
            self.identifier = self.choice()

    def choice(self):
        # Cluster yearbook selections within the childhoods of most of
        # the people who will be seeing this.
        self.year = int(random.gauss(1980, 20))
        for_year = self.by_year.get(str(self.year))
        if not for_year:
            return None
        return random.choice(for_year)

    def post(self):
        item = Text(self.identifier)
        pages = item.pages or 200
        page = random.randint(0, pages-1)
        reader_url = item.reader_url(page)
        image_url = item.image_url(page)
        response = requests.head(image_url)
        if response.status_code != 200:
            return None, None, None, None
        return item.metadata.get('title', ''), self.year, reader_url, image_url
