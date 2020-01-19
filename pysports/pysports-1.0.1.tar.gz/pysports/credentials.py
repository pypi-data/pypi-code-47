# User and API Credentials are here.
class Credentials(object):
    def __init__(self, apikey, host):
        self.apikey = apikey
        self.url = host

    def get_url(self):
        return dict(url=self.url)

    def get_apikey(self):
        return dict(apikey=self.apikey)

    def get_headers(self):
        return dict()