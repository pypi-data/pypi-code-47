import requests
from bbdata.config import output_api_url
from bbdata.util import handle_response


class Units:

    base_path = "/units"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self):
        """
        GET /units
        https://bbdata.daplab.ch/api/#units_get
        """
        url = output_api_url + self.base_path
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def post(self, name, symbol, unit_type):
        """
        POST /units
        https://bbdata.daplab.ch/api/#units_post
        """
        # TODO Finish the implementation and test it
        data = {
            "name": name,
            "symbol": symbol,
            "type": unit_type
        }
        url = output_api_url + self.base_path
        r = requests.post(url, data, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

