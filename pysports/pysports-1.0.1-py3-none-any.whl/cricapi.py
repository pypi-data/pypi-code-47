import requests
from pysports.credentials import Credentials


class CricAPI(Credentials):
    def __init__(self, *args):
        super(CricAPI, self).__init__(*args)
        self.data = {}

    def get_params(self, apikey=False, match_id=False, player_id=False):
        if apikey and match_id:
            return dict(apikey=apikey, unique_id=match_id)
        elif apikey and player_id:
            return dict(apikey=apikey, pid=player_id)
        elif apikey:
            return dict(apikey=apikey)

    def upcoming_matches(self):
        url_endpoint = "matches/"
        url = self.url + url_endpoint
        req = requests.get(url, params=self.get_params(self.apikey))
        self.data.clear()
        self.data = {**req.json()}
        return self.data

    def historical_matches(self):
        url_endpoint = "cricket/"
        url = self.url + url_endpoint
        req = requests.get(url, params=self.get_params(self.apikey))
        self.data = {**req.json()}
        return self.data

    def match_summary(self, match_id):
        url_endpoint = "fantasySummary/"
        url = self.url + url_endpoint
        req = requests.get(url, params=self.get_params(self.apikey, match_id))
        self.data = {**req.json()}
        return self.data

    def live_score(self, match_id):
        url_endpoint = "cricketScore/"
        url = self.url + url_endpoint
        req = requests.get(url, params=self.get_params(self.apikey, match_id))
        self.data = {**req.json()}
        return self.data

    def about_player(self, player_id):
        url_endpoint = "playerStats/"
        url = self.url + url_endpoint
        req = requests.get(url, params=self.get_params(self.apikey, False, player_id))
        self.data = {**req.json()}
        return self.data
