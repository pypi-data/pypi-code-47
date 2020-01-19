import base64
import urllib

import requests

from .BasicUtilClass import BaseUtilClass


class HttpSession(BaseUtilClass):
    def __init__(self, logger, endpoint=None, timeout=5):
        super().__init__(logger)
        session = requests.Session()
        session.headers = {}
        session.timeout = timeout
        self.endpoint = endpoint
        self.session = session

    def set_http_basic_auth_headers(self, username, token):
        encoding = self.encoding if hasattr(self, 'encoding') else 'utf-8'
        auth_bs64_encode_str = base64.b64encode(f"{username}:{token}".encode(encoding)).decode(encoding)
        auth_header = {"Authorization": "Basic " + auth_bs64_encode_str}
        if hasattr(self.session, 'headers'):
            self.session.headers.update(auth_header)
        else:
            self.session.headers = auth_header

    def request_conn(self, path, method='get', data=None):
        if path.startswith("http://") or path.startswith("https://"):
            requests_path = path
        elif path.startswith("/"):
            requests_path = f'{self.endpoint}{path}'
        else:
            self.logger.warning(f"Un supported path schema {path}")

        requests_params = dict(
            headers=self.session.headers,
            verify=False,
            timeout=self.session.timeout,
        )

        if self.session.headers.get('Content-Type') in ["application/json"]:
            requests_params["json"] = data
        elif self.session.headers.get("Content-Type") in ["application/x-www-form-urlencoded"]:
            requests_params["data"] = urllib.parse.urlencode(data)
        else:
            requests_params["data"] = data
        try:
            conn = self.session.request(method, requests_path, **requests_params)
            self.logger.info(f'{method} url {requests_path}')
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as Error:
            print(Error)
            conn = None
        return conn

    def read_json(self, path):
        conn = self.request_conn(path)
        return None if conn is None else conn.json()
