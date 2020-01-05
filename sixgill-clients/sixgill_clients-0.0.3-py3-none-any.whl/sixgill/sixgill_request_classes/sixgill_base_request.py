from abc import ABC, abstractmethod
from urllib.parse import urljoin

from requests import Request, Session


class SixgillBaseRequest(ABC):
    SIXGILL_API_BASE_URL = 'https://api.cybersixgill.com/'

    def __init__(self, channel_code, *args, **kwargs):
        self.__session = Session()
        self.request = Request(self.method, self._get_url(), **kwargs)

        self.request.headers['Cache-Control'] = 'no-cache'
        self.request.headers['Channel-Code'] = channel_code

    @property
    @abstractmethod
    def end_point(self):
        pass

    @property
    @abstractmethod
    def method(self):
        pass

    def _get_url(self):
        return urljoin(self.SIXGILL_API_BASE_URL, self.end_point)

    def send(self):
        return self.__session.send(request=self.request.prepare(), verify=False)
