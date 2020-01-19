"""A REST client for the Frontegg API."""

import typing
from abc import ABCMeta, abstractmethod
from urllib.parse import urljoin

import arrow
import requests

from frontegg.permissions import FronteggPermissions, validate_permissions

RequestT = typing.TypeVar('RequestT')


class FronteggContext:
    """Request context."""

    __slots__ = ('_user_id', '_tenant_id', '_permissions')

    def __init__(self,
                 user_id: str,
                 tenant_id: str,
                 permissions: typing.List[FronteggPermissions] = (FronteggPermissions.All,)) -> None:
        """

        :param user_id:
        :param tenant_id:
        :param permissions:
        """
        self._user_id = user_id
        self._tenant_id = tenant_id
        self._permissions = permissions

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def tenant_id(self) -> str:
        return self._tenant_id

    @property
    def permissions(self) -> typing.List[FronteggPermissions]:
        return self._permissions


class BaseFronteggClient(typing.Generic[RequestT], metaclass=ABCMeta):
    """A REST client for the Frontegg API."""

    def __init__(self,
                 client_id: str,
                 api_key: str,
                 context_callback: typing.Callable[[RequestT], FronteggContext]) -> None:
        """Initialize the Frontegg client.

        :param client_id: The client ID provided to you by Frontegg
        :param api_key: The secret key provided to you by Frontegg
        :param context_callback: A callable which accepts the current request as an argument
            and returns the frontegg context based on the request.
        """
        self.api_key = api_key
        self.client_id = client_id
        self.context_callback = context_callback
        self.session = requests.Session()
        self._api_token = None
        self._expires_in = None

    def _maybe_refresh_api_token(self) -> None:
        """Refresh the API token if it is not present or about to expire."""
        if self._api_token is None or self._expires_in is None or arrow.utcnow() >= self._expires_in:
            self._refresh_api_token()

    def _refresh_api_token(self) -> None:
        """Refresh the API token.

        This function retrieves a new API token from the Frontegg API.

        :raises requests.HTTPError: If the Frontegg API responds with an HTTP error code, this exception is raised.
        """
        auth_response = self.session.post(self.authentication_service_url,
                                          data={
                                              'clientId': self.client_id,
                                              'secret': self.api_key
                                          })
        auth_response.raise_for_status()

        auth_response_data = auth_response.json()
        self._api_token = auth_response_data['token']
        self._expires_in = arrow.utcnow().shift(
            seconds=auth_response_data['expiresIn'] * 0.8)

    @property
    @abstractmethod
    def base_url(self) -> str:
        pass

    @property
    @abstractmethod
    def authentication_service_url(self) -> str:
        pass

    @property
    def api_token(self) -> str:
        """The API Token to use to authenticate against Frontegg's services.

        :return: The API token.
        :raises requests.HTTPError: If the Frontegg API responds with an HTTP error code, this exception is raised.
        """
        self._maybe_refresh_api_token()
        return self._api_token

    @property
    @abstractmethod
    def current_request(self) -> RequestT:
        pass

    @property
    def context(self) -> typing.Optional[FronteggContext]:
        """The context under which the request is proxied.

        :return: The :class:`FronteggContext` result from the callback.
        """
        context = self.context_callback(self.current_request)

        if context:
            return context

        return None

    def request(self,
                endpoint: str,
                method: str,
                data: typing.Optional[dict] = None,
                tenant_id: typing.Optional[str] = None) -> requests.Response:
        """Perform a request to Frontegg's API.

        :param endpoint: The endpoint to perform the request to.
        :param method: The HTTP method to use while performing the request.
        :param data: When performing a GET request, the query string to pass as part of the request, if applicable..
            In any other request, the JSON payload to pass as the body of the request, if applicable.
        :param tenant_id: Override the tenant id from the context.
        :return: The response of the request.
        :raises requests.HTTPError: If the Frontegg API responds with an HTTP error code, this exception is raised.
        """
        context = self.context
        if tenant_id:
            user_id = None
        else:
            user_id, tenant_id = context.user_id, context.tenant_id

        if context:
            permissions = context.permissions
        else:
            permissions = (FronteggPermissions.All,)
        validate_permissions(endpoint, method, permissions=permissions)

        headers = {
            'x-access-token': self.api_token,
        }
        if tenant_id:
            headers['frontegg-tenant-id'] = tenant_id
        if user_id:
            headers['frontegg-user-id'] = user_id

        if method.upper() == 'GET':
            kwargs = {
                'params': data
            }
        else:
            kwargs = {
                'data': data
            }

        return self.session.request(
            method,
            urljoin(self.base_url, endpoint),
            headers=headers,
            **kwargs
        )


class FronteggClient(BaseFronteggClient[None]):
    """A standalone Frontegg REST client."""

    def __init__(self,
                 client_id: str,
                 api_key: str,
                 context_callback: typing.Callable[[RequestT], FronteggContext],
                 base_url: str = 'https://api.frontegg.com/',
                 authentication_service_url: str = None) -> None:
        """Initialize the Frontegg client.

        :param client_id: The client ID provided to you by Frontegg.
        :param api_key: The secret key provided to you by Frontegg.
        :param context_callback: A callable which returns the user id and tenant id based on the current request.
        :param base_url: The base URL of the API.
        :param authentication_service_url: The URL for authenticating against Frontegg.
        """
        super().__init__(client_id, api_key, context_callback)
        self._base_url = base_url

        if authentication_service_url:
            self._authentication_service_url = authentication_service_url
        else:
            self._authentication_service_url = urljoin(
                base_url, '/vendors/auth/token')

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def authentication_service_url(self) -> str:
        return self._authentication_service_url

    @property
    def current_request(self):
        return None


__all__ = ('BaseFronteggClient', 'FronteggClient')
