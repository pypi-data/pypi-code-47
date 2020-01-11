"""Main module."""
import base64
import re
import hashlib
import requests
from datetime import datetime
from aiohttp.hdrs import (
    CONTENT_TYPE, 
    COOKIE, 
    REFERER, 
    ACCEPT,
    PRAGMA,
    CONNECTION,
    KEEP_ALIVE,
    USER_AGENT,
    CACHE_CONTROL,
    ACCEPT_ENCODING,
    ACCEPT_LANGUAGE,
)

HTTP_HEADER_X_REQUESTED_WITH = "X-Requested-With"
HTTP_HEADER_NO_CACHE = "no-cache"


class TpLinkEAPClient(object):
    def __init__(self, password, host='192.168.1.1', username=None):
        self.host = host
        self.password = password
        self.username = username
        self.parse_macs = re.compile(
            "[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-"
            + "[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}"
        )

        self.parse_names = re.compile('hostName=(.*)')

    def get_connected_devices(self):
        base_url = f"http://{self.host}"
        header = {
            USER_AGENT: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12;"
            " rv:53.0) Gecko/20100101 Firefox/53.0",
            ACCEPT: "application/json, text/javascript, */*; q=0.01",
            ACCEPT_LANGUAGE: "Accept-Language: en-US,en;q=0.5",
            ACCEPT_ENCODING: "gzip, deflate",
            CONTENT_TYPE: "application/x-www-form-urlencoded; charset=UTF-8",
            HTTP_HEADER_X_REQUESTED_WITH: "XMLHttpRequest",
            REFERER: f"http://{self.host}/",
            CONNECTION: KEEP_ALIVE,
            PRAGMA: HTTP_HEADER_NO_CACHE,
            CACHE_CONTROL: HTTP_HEADER_NO_CACHE,
        }
        password_md5 = hashlib.md5(self.password.encode("utf")).hexdigest().upper()

        # Create a session to handle cookie easier
        session = requests.session()
        session.get(base_url, headers=header)

        login_data = {"username": self.username, "password": password_md5}
        session.post(base_url, login_data, headers=header)

        # A timestamp is required to be sent as get parameter
        timestamp = int(datetime.now().timestamp() * 1e3)

        client_list_url = f"{base_url}/data/monitor.client.client.json"

        get_params = {"operation": "load", "_": timestamp}

        response = session.get(client_list_url, headers=header, params=get_params)
        session.close()
        try:
            list_of_devices = response.json()
        except ValueError:
            return {}

        return {
            device["MAC"].replace("-", ":"): device["DeviceName"]
            for device in list_of_devices["data"]
        }