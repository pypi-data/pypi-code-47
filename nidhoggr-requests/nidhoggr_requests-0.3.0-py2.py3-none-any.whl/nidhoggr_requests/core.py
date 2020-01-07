from abc import ABCMeta
from typing import Dict, Any, Union

from nidhoggr_core.response import StatusResponse
from requests import Session, RequestException


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

    def fetch(self, *, endpoint: str, payload: Dict[str, Any]) -> Union[StatusResponse, Dict[str, Any]]:
        try:
            response = self._session.post(f'{self._api_url}{endpoint}', json=payload, timeout=self._timeout)
        except RequestException as e:
            return StatusResponse(status=False, reason=f"Failed to fetch {endpoint} due to {e}")

        if response.status_code != 200:
            return StatusResponse(status=False, reason=f"Expected 200, got {response.status_code} for {endpoint}")

        result = response.json()
        if not result:
            return StatusResponse(status=False, reason=f"Response from {endpoint} didn't contain valid JSON")
        return result
