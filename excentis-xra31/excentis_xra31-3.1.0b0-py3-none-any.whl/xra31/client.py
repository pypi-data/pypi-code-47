"""A Python client for the XRA-31."""

import logging
import time

import requests

from . import analysis, capture, configuration, decorate, exceptions
from .trace import trace


class Client:
    """A Python client for the XRA-31."""
    @decorate.translate_requests
    def __init__(self, address: str = "localhost"):
        """Create a connection with an XRA-31.

        :param address: Address of the XRA-31.
        :type address: str, optional
        """
        #: The XRA-31's address.
        self.address = address
        self.token = -1
        self._session = requests.Session()
        self._session_time = time.monotonic()
        #: The XRA-31's request timeout in seconds (read/connect).
        self.timeout = 10.

        #: The :class:`~excentis.xra31.configuration.Configuration` object.
        self.configuration = configuration.Configuration(self)
        #: The :class:`~excentis.xra31.capture.Capture` object.
        self.capture = capture.Capture(self)
        #: The :class:`~excentis.xra31.analysis.Analysis` object.
        self.analysis = analysis.Analysis(self)

        response = self._session.get(self.url_api + "/system/customer",
                                     timeout=self.timeout)
        response.raise_for_status()
        response_json = response.json()

        #: The XRA-31's system serial.
        self.system_serial = response_json["system_serial"]
        #: The XRA-31's licensed company.
        self.company = response_json["company"]

        self.logger = logging.getLogger(__package__)

    def __enter__(self):
        self.get_full_access()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.release()

    def __bool__(self):
        return self.token != -1

    @property
    def session(self) -> requests.Session:
        # pylint: disable=missing-function-docstring
        now = time.monotonic()
        if now - self._session_time < .05:
            time.sleep(.05 - now + self._session_time)
        self._session_time = time.monotonic()
        return self._session

    @property
    def url(self) -> str:
        """The XRA-31's URL."""
        return "http://{address}".format(address=self.address)

    @property
    def url_api(self) -> str:
        """The XRA-31's API URL."""
        return "http://{address}/api/v1".format(address=self.address)

    @decorate.translate_requests
    @trace
    def get_full_access(self) -> None:
        """Enter full access mode."""
        if self:
            return
        response = self.session.get(self.url_api + "/system/privilegeToken",
                                    params={'forced': 'true'},
                                    timeout=self.timeout)
        response.raise_for_status()
        self.token = response.json()["privilegeToken"]
        self._session.headers["x-privilegetoken"] = str(self.token)

    @decorate.translate_requests
    @trace
    def try_full_access(self) -> bool:
        """Try to enter full access mode.

        :return: ``True`` if successful, ``False`` otherwise.
        :rtype: bool
        """
        if self:
            return True
        response = self.session.get(self.url_api + "/system/privilegeToken",
                                    timeout=self.timeout)
        if not response.ok:
            return False
        self.token = response.json()["privilegeToken"]
        self._session.headers["x-privilegetoken"] = str(self.token)
        return True

    @trace
    def require_capture_active(self, active: bool = True):
        # pylint: disable=missing-function-docstring
        if self.capture.active != active:
            raise exceptions.Xra31StateException

    @trace
    def require_full_access(self, full_access: bool = True) -> None:
        # pylint: disable=missing-function-docstring
        if self.try_full_access() != full_access:
            raise exceptions.Xra31FullAccessException

    @decorate.translate_requests
    @trace
    def release(self) -> None:
        """Release full access mode."""
        if not self:
            return
        request = requests.Request('DELETE',
                                   self.url_api + "/system/privilegeToken")
        prepped = self._session.prepare_request(request)
        self.token = -1
        self._session.headers.pop("x-privilegetoken")
        response = self.session.send(prepped, timeout=self.timeout)
        response.raise_for_status()

    def __str__(self) -> str:
        return "{} ({}) at {}".format(self.system_serial, self.company,
                                      self.url)

    @trace
    def describe(self) -> dict:
        """Representation of an XRA-31 configuration."""
        description = {}
        description["configuration"] = self.configuration.describe()
        description["capture"] = self.capture.describe()
        return description

    @trace
    def apply(self, description: dict) -> None:
        """Apply an XRA-31 configuration.

        :param description: The configuration description (:func:`describe`).
        :type description: dict
        """
        self.require_full_access()
        self.require_capture_active(False)
        if "configuration" in description:
            self.configuration.apply(description["configuration"])
        if "capture" in description:
            self.capture.apply(description["capture"])
