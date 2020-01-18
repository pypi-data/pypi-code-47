import requests
from requests.models import Response
from loguru import logger
import json
import typing


class J2DBClient(object):
    def __init__(
        self, ip_address: str, port: int, table: str = None, secret: str = None
    ):
        self.ip_address: str = ip_address
        self.port: int = port
        self.root_url = f"http://{self.ip_address}:{self.port}"
        self.upload_url = f"{self.root_url}/api/json/form"

        self.table: str = table or ""
        # support insert only
        self.action: str = "insert"
        self.secret: str = secret or ""

        # check
        logger.info(f"bind to server: {self.root_url}")
        assert self.heartbeat(), "connection failed"

    def heartbeat(self) -> bool:
        return requests.get(self.root_url).ok

    def send(
        self, content: typing.Union[str, dict], table: str = None, secret: str = None
    ) -> Response:
        table = table or self.table
        secret = secret or self.secret
        assert table, "no table configured"
        assert secret, "no secret configured"

        if isinstance(content, dict):
            content = json.dumps(content)
        logger.info(f"request with data: {content}")

        request_data = {
            "table": table,
            "action": self.action,
            "content": content,
            "secret": secret,
        }
        resp = requests.post(self.upload_url, data=request_data)
        if not resp.ok:
            logger.warning("response status seems not good")
        if resp.json()["error"] != "":
            logger.warning("error happened in response")
        return resp
