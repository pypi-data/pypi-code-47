"""
Adapter to make requests to 17track API
"""
import json
from typing import Dict, Union

from track17.client import Response, Track17Client

__all__ = (
    'Track17Adapter',
)


class Track17Adapter:
    api_client_class = Track17Client

    def __init__(self):
        self.api_client = self.api_client_class()

    @staticmethod
    def _prepare_numbers(*tracking_numbers: Union[Dict, str]) -> str:
        numbers = []
        for number in tracking_numbers:
            if isinstance(number, dict) and all(
                    key in number for key in ['number', 'carrier']
            ):
                numbers.append(number)
            elif isinstance(number, str):
                numbers.append({
                    "number": number
                })
        numbers = json.dumps(numbers)
        return numbers

    def register(self, *tracking_numbers: str) -> Response:
        """
        40 tracking numbers are allowed to submit for registration per time for the interface.

        Response:
            {
                "code": 0,
                "data": {
                    "accepted": [
                        {
                            "number": "RR123456789CN",
                            "carrier": 3011
                        }
                    ],
                    "rejected": [
                        {
                            "number": "1234",
                            "error": {
                                "code": -18010012,
                                "message": "The format of '1234' is invalid."
                            }
                        }
                    ]
                }
            }
        """
        data = self._prepare_numbers(*tracking_numbers)
        response = self.api_client.post(
            'register',
            data
        )
        return response

    def stop_track(self, *tracking_numbers: str) -> Response:
        """
        40 tracking numbers are allowed to submit per time for the interface.
        """
        data = self._prepare_numbers(*tracking_numbers)
        response = self.api_client.post(
            'stoptrack',
            data
        )
        return response

    def retrack(self, *tracking_numbers: str) -> Response:
        """
        40 tracking numbers are allowed to submit per time for the interface.
        """
        data = self._prepare_numbers(*tracking_numbers)
        response = self.api_client.post(
            'retrack',
            data
        )
        return response

    def get_track_info(self, *tracking_numbers: str) -> Response:
        """
        40 tracking numbers are allowed to submit per time for the interface.
        """
        data = self._prepare_numbers(*tracking_numbers)
        response = self.api_client.post(
            'gettrackinfo',
            data
        )
        return response
