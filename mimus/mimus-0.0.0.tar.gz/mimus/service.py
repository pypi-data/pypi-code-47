"""
service contains request-serving entities.
"""

from enum import Enum

from .handler import noop


class Protocol(Enum):
    """
    Protocol is an enum of all the supported layer 7 protocols. Currently
    only http(s) is supported
    """
    HTTP = 'http'
    HTTPS = 'https'


class Service:
    """
    Service defines the endpoint and the handler to serve incoming requests.

    Most of the fields are for TCP layer.
    """

    def __init__(self, name, host, port, protocol, handler=None, meta=None):
        super().__init__()

        self.name = name
        self.host = host
        self.port = port
        self.protocol = protocol
        self.handler = handler or noop
        self.meta = meta or {}

    def match(self, request):
        """
        match returns if the request should be handled by the service.
        """
        return (
            request.host == self.host and
            request.port == self.port and
            request.protocol == self.protocol
        )

    def handle(self, request):
        """
        handle handles the request.
        """
        return self.handler(request)


class HTTPService(Service):
    """
    HTTPService defines the http(s) parameters to serve incoming requests.
    """

    def __init__(self,
                 name,
                 host,
                 port=80,
                 method="get",
                 params=None,
                 path="",
                 handler=None):
        super().__init__(
            name, host, port, protocol=Protocol.HTTP, handler=handler)

        self.method = method
        self.params = params
        self.path = path or "/"

    def match(self, request):
        if not super().match(request):
            return False

        if request.method != self.method:
            return False

        if not _match_path(self.path, request.path):
            return None

        if not _match_params(self.params, request.params):
            return False

        return True


def _match_path(cond, _):
    # TODO: path matching
    return cond is None


def _match_params(conds, params):
    # TODO: parameter matching
    return conds is None and params is None
