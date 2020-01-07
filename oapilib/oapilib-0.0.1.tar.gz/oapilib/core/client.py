"""HTTP Client Interface module.

Implement the 'OAPI - Common' client interface for accessing
various implementations.

Classes: OAPIRequestInterface

Functions: fetch()
"""
import json
from enum import Enum
from typing import Any, List, Optional, Tuple

from httpx import AsyncClient
from pydantic import AnyHttpUrl as AnyHttpURL
from pydantic import BaseModel, root_validator


class FormatEnum(str, Enum):
    """Enumerate available encodings."""

    JSON: str = "json"
    HTML: str = "html"


class ContentTypeEnum(str, Enum):
    """Enumerate available content types."""

    JSON: str = '{"Content-Type": "application/json"}'
    HTML: str = '{"Content-Type": "text/html"}'


class BaseRequestInterface(BaseModel):
    """BaseRequestInterface class is used to hold the client.

    Parameters
    ----------
    BaseModel : Pydantic BaseModel

    Attributes
    ----------
    url : str
        URL/URI of the resource
    f : str
        Encoding format for the resource
    headers : list
        Array with the headers to access the resource

    Raises
    ------
    ValueError
        Validation error if the format encoding is not
        consistent with the requested content type
    """

    url: AnyHttpURL = None
    f: FormatEnum = FormatEnum.JSON
    headers: List[dict] = [json.loads(ContentTypeEnum.JSON)]

    @root_validator
    def check_content_consistency(cls, values):
        """Validate consistency of encoding and content type.

        Parameters
        ----------
        values : dict
            The values of attributes from the instance

        Raises
        ------
        ValueError
            Validation error with custom Pydantic error message
        """
        content_type = [
            item.get("Content-Type")
            for item in values["headers"]
            if "Content-Type" in item.keys()
        ][0]
        if values["f"] != content_type.partition("/")[2]:
            raise ValueError("Content type and format do not match!")
        return values


class OAPIRequestInterface(BaseRequestInterface):
    """Define generic interface for OGC API.

    Examples
    --------
    >>>oapiri = OAPIRequestInterface(
        url='https://demo.pygeoapi.io/master/collections/countries')
    """

    @property
    def scheme(self):
        """Get the scheme from a given URL/URI.

        Returns
        -------
        str
            Returns a string of the OAPI implementation scheme.

        Examples
        --------
        >>>oapiri = OAPIRequestInterface(
            url='https://demo.pygeoapi.io/master/collections/countries')
        >>>oapiri.scheme
        'https'
        """
        return self.url.scheme

    @property
    def host(self):
        """Get the host from a given URL/URI.

        Returns
        -------
        str
            Returns a string of the OAPI implementation host.

        Examples
        --------
        >>>oapiri = OAPIRequestInterface(
            url='https://demo.pygeoapi.io/master/collections/countries')
        >>>oapiri.host
        'demo.pygeoapi.io'
        """
        return self.url.host

    @property
    def port(self):
        """Get the port from a given URL/URI.

        Returns
        -------
        str
            Returns a string of the OAPI implementation port.

        Examples
        --------
        >>>oapiri = OAPIRequestInterface(
            url='https://demo.pygeoapi.io/master/collections/countries')
        >>>oapiri.port
        '443'
        """
        if self.url.port:
            return self.url.port
        else:
            if self.scheme == "https":
                return "443"
            elif self.scheme == "http":
                return "80"
            else:
                raise ValueError("Wrong scheme detected")

    @property
    def path(self):
        """Get the resource path from a given URL/URI.

        Returns
        -------
        str
            Returns a string of the OAPI requested whole resource path.

        Examples
        --------
        >>>oapiri = OAPIRequestInterface(
            url='https://demo.pygeoapi.io/master/collections/countries')
        >>>oapiri.path
        '/master/collections/countries'
        """
        if not self.url.path:
            return f"/"
        return self.url.path

    @property
    def query(self):
        """Get the query string from a given URL/URI.

        Returns
        -------
        str
            Returns a string of the query string for the
            OAPI requested resource path.

        Examples
        --------
        >>>oapiri = OAPIRequestInterface(
            url='https://demo.pygeoapi.io/master/collections/countries')
        >>>oapiri.query
        'f=json'
        """
        if not self.url.query:
            return f"f={self.f.value}"
        return self.url.query

    @property
    def base_url(self) -> AnyHttpURL:
        """Get a validated http base URL from a given URL/URI.

        Returns
        -------
        AnyHttpURL
            Returns a validated URL of type Pydantic AnyHttpURL

        Examples
        --------
        >>>oapiri = OAPIRequestInterface(
            url='https://demo.pygeoapi.io/master/collections/countries')
        >>>oapiri.base_url
        'https://demo.pygeoapi.io'
        """
        build_url = f"{self.scheme}://{self.host}"
        if self.port not in ("443", "80"):
            build_url = f"{build_url}:{self.port}"
        return build_url

    @property
    def prefix_path(self) -> Optional[str]:
        """Get the prefix path for a given URL/URI.

        Returns
        -------
        str
            Returns a string of the prefix path for the
            OAPI requested resource.

        Examples
        --------
        >>>oapiri = OAPIRequestInterface(
            url='https://demo.pygeoapi.io/master/collections/countries')
        >>>oapiri.prefix_path
        '/master'
        """
        prefix = self._partitioned_oapi_path()[0]
        if prefix == "/":
            prefix = f""
        return prefix

    @property
    def oapi_resource(self) -> Optional[str]:
        """Get the OAPI resource path for a given URL/URI.

        Returns
        -------
        str
            Returns a string of the relative path for the
            OAPI requested resource.

        Examples
        --------
        >>>oapiri = OAPIRequestInterface(
            url='https://demo.pygeoapi.io/master/collections/countries')
        >>>oapiri.prefix_path
        '/collections/countries'
        """
        resource = (
            f"{self._partitioned_oapi_path()[1]}" f"{self._partitioned_oapi_path()[2]}"
        )
        return resource

    def _partitioned_oapi_path(self) -> Tuple:
        """Partition an oapi path by 'collections'.

        Returns
        -------
        tuple
            Returns the splitted parts of the path between the
            'collections' location
        """
        return self.path.partition("/collections")

    async def fetch(self) -> Any:
        """Get the content for a given URL/URI.

        Returns
        -------
        dict
            Content of the OAPI resource
        """
        # with AsyncClient as client:
        #     print(self.url)
        #     resp = await client.get(self.url)
        # return resp.json
        client = AsyncClient()
        response = await client.get(self.url)
        # return json.dumps(response.json(), indent=4, sort_keys=True)
        return response.json()
