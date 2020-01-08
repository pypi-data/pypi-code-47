from enum import Enum
import requests
from bbdata.config import output_api_url
from bbdata.util import handle_response
from bbdata.exceptions import ClientException

class Aggregation(Enum):
    QUARTERS = "quarters"
    HOURS = "hours"


class Values:

    base_path = "/values"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get(self, object_id, from_timestamp, to_timestamp, with_comments=False, headers=True):
        """
        Get measures.

        GET /values
        https://bbdata.daplab.ch/api/#values_get
        """
        params = {
            "ids": object_id,
            "from": from_timestamp,
            "to": to_timestamp,
            "withComments": with_comments,
            "headers": headers
        }

        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def get_latest(self, object_id, before_timestamp, with_comments=False):
        """
        Get the latest measure before a given date, if any. Note that the
        lookup won't go further than six month in time. This means that if the
        object didn't deliver any value in the six month before the "before"
        parameter, no value will be returned.

        GET /values/latest
        https://bbdata.daplab.ch/api/#values_latest_get
        """
        params = {
            "ids": object_id,
            "before": before_timestamp,
            "withComments": with_comments,
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def get_hours(self, object_id, from_timestamp, to_timestamp, with_comments=False, headers=True):
        """
        # TODO No definition in the docs
        GET /values/hours
        """
        return self.__aggregation(object_id, from_timestamp, to_timestamp, "hours", with_comments, headers)

    def get_quarters(self, object_id, from_timestamp, to_timestamp, with_comments=False, headers=True):
        """
        # TODO No definition in the docs
        GET /values/quarters
        """
        return self.__aggregation(object_id, from_timestamp, to_timestamp, "quarters", with_comments, headers)

    def __aggregation(self, object_id, from_timestamp, to_timestamp, aggregation, with_comments=False, headers=True):
        """
        Generic method to call the aggregations implemented in the API
        """
        params = {
            "ids": object_id,
            "from": from_timestamp,
            "to": to_timestamp,
            "withComments": with_comments,
            "headers": headers
        }

        url = output_api_url + self.base_path

        if aggregation == Aggregation.HOURS.value:
            url = url + "/hours"
        elif aggregation == Aggregation.QUARTERS.value:
            url = url + "/quarters"
        else:
            raise ClientException("This aggregation isn't implemented")

        r = requests.get(url, params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())
