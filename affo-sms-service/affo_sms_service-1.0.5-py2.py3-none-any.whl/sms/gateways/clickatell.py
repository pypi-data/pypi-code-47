import requests

from affo_sms_service import settings

from .base import BaseSMSGateway
from .. import exception


class Client:
    CLICKATELL_ENDPOINT_URL = "https://platform.clickatell.com"

    def __init__(self, api_key) -> None:
        self.session = requests.Session()
        self.session.headers = {"authorization": api_key, "content-type": "application/json", "x-version": "1"}

    def request(self, path, **kwargs):
        url = f"{self.CLICKATELL_ENDPOINT_URL}{path}"

        return self.session.request(url=url, **kwargs)

    def send_message(self, to, body):
        if isinstance(to, str):
            to = [to]

        response = self.request(method="POST", path="/messages", json={"content": body, "to": to})
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            raise exception.SMSError(f"{e}:\n\n{e.response.text}")

        response_data = response.json()

        for message in response_data["messages"]:
            if message["accepted"] is not True:
                if message["errorCode"] == 652:
                    raise exception.InvalidPhone(message["errorDescription"])
                raise exception.SMSError(message["errorDescription"])


class ClickatellGateway(BaseSMSGateway):
    name = "clickatell"

    def __init__(self):
        super().__init__()
        self.client = Client(api_key=settings.CLICKATELL_API_KEY)

    def send(self, to: str, from_: str, body: str):
        self.client.send_message(to=to, body=body)
