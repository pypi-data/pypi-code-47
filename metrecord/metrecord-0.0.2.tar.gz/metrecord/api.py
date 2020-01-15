from concurrent.futures import ThreadPoolExecutor

import requests

from metrecord.exceptions import MetrecordAPIException

_BASE_URL = 'https://api.metrecord.com'
HEADERS = {'Content-Type': 'application/json'}

class Metrecord(object):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.pool = ThreadPoolExecutor(max_workers=4)

    def track(self, metric, value):
        self.pool.submit(self._track, metric, value)

    def _track(self, metric, value, raise_on_failure=False):
        payload = {
            'metric': metric,
            'value': value,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        url = _BASE_URL + '/api/events'
        res = requests.post(url, headers=HEADERS, json=payload)
        if res.status_code != 201:
            if raise_on_failure:
                raise MetrecordAPIException(res.status_code, 'Internal Error')
            else:
                return False
        return True
