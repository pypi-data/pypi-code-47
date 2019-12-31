from abc import ABCMeta
from typing import Dict, Any, Optional

from requests import Session


class RequestsRepo(metaclass=ABCMeta):
    _session: Session
    _api_url: str
    _timeout: int

    def __init__(self, *, api_url: str, bearer_token: str, timeout: int = 1):
        session = Session()
        session.headers.update({
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json'
        })
        self._session = session
        self._api_url = api_url
        self._timeout = timeout

    def fetch(self, *, endpoint: str, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        response = self._session.post(f'{self._api_url}{endpoint}', json=payload, timeout=self._timeout)
        if response.status_code != 200:
            return None
        result = response.json()
        if not result:
            return None
        return result
