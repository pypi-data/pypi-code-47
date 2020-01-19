import functools
import requests
import urllib
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict
API_Token = 'C3310BE5BBB93CE82D142EADC87FD96B'

class BaseAPI(object):
    """Base wrapper for individual AC Transit APIs"""
    BASE_URL = "https://api.actransit.org/transit"
    api = ''
    key = ''
    protobuf = ''

    def __init__(self, key):
        self.base_url = self.BASE_URL.format(api=self.api)
        self.key = key

    def __repr__(self):
        return "BaseAPI{obj}".format(obj=object)

    def get_protobuf(self):
        """
        Gets protocol buffer file from the specified URL.
        """
        try:
            with urllib.request.urlopen(self.url) as response:
                self.protobuf.ParseFromString(response.read())
                feed_dictionary = protobuf_to_dict(self.protobuf)

        except urllib.error.URLError:
            raise RuntimeError("No Internet Connection")

        return feed_dictionary

    def get_json(self):
        """
        Gets JSON file prom the specified URL.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except (requests.exceptions.ConnectionError):
            raise RuntimeError("No Internet Connection")

        return response.json()


def api_method(method):
    """Decorator for using method signatures to validate and make API calls."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Validate arguments
        method(self, *args, **kwargs)

        # Create URL
        self.url = "{base_url}/{base_api}/{api}?token={key}".format(
            base_url=self.base_url,
            base_api=self.api,
            api=method.__name__,
            key=self.key
        )

        # Generate API response
        if self.protobuf:
            api_response = self.get_protobuf()
        else:
            api_response = self.get_json()

        return api_response

    return wrapper


class GTFSRT(BaseAPI):
    """API for real time General Transit Feed Specifications:
    https://api.actransit.org/transit/gtfsrt/"""
    api = 'gtfsrt'
    protobuf = gtfs_realtime_pb2.FeedMessage()

    def __repr__(self):
        return "ACTransit(GTFSRT(api_key))"

    @api_method
    def alerts(self):
        pass

    @api_method
    def tripupdates(self):
        pass

    @api_method
    def vehicles(self):
        pass


class GTFS(BaseAPI):
    """API for General Transit Feed Specifications:
    https://api.actransit.org/transit/gtfs/"""
    api = 'gtfs'

    def __repr__(self):
        return "ACTransit(GTFS(api_key))"

    @api_method
    def all(self):
        pass


class ACTransit(object):
    """Wrapper for the AC Transit API."""
    gtfsrt = None
    gtfs = None

    def __init__(self, key=API_Token):
        """Initialize the individual APIs with the API key."""
        args = (key,)
        self.gtfsrt = GTFSRT(*args)
        self.gtfs = GTFS(*args)

    def __repr__(self):
        return "ACTransit()"
