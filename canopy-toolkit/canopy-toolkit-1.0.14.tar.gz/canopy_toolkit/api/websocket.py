import asyncio
import json
from contextlib import asynccontextmanager
from typing import Dict
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

import websockets
from requests import HTTPError
from websockets import WebSocketClientProtocol

from canopy_toolkit.api.base import BaseCanopyClient, CanopyResponse
from canopy_toolkit.api.exceptions import CanopyAPIException


class WebsocketResponse:
    """A websocket response."""

    status_code: int
    _response: Dict

    def __init__(self, status_code: int, response: Dict):
        """
        Create an instance of a websocket response.

        :param status_code: The status code
        :param response: the dictionary response
        """
        self.status_code = status_code
        self._response = response

    def json(self):
        """
        Get response as json.

        :return: the json response
        """
        return self._response

    def text(self):
        """
        Get response as string.

        :return: the response as string
        """
        return json.dumps(self._response)

    @property
    def ok(self):
        """Return True if :attr:`status_code` is less than 400, False if not.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        """
        try:
            self.raise_for_status()
        except HTTPError:
            return False
        return True

    def raise_for_status(self):
        """Raise stored :class:`HTTPError`, if one occurred."""
        http_error_msg = ''

        if 400 <= self.status_code < 500:
            http_error_msg = u'%s Client Error' % self.status_code

        elif 500 <= self.status_code < 600:
            http_error_msg = u'%s Server Error' % self.status_code

        if http_error_msg:
            raise HTTPError(http_error_msg, response=self)


class CanopyWebsocketClient:
    """The base websocket client."""

    _base_client: BaseCanopyClient

    def __init__(self, base_client: BaseCanopyClient):
        """
        Create a websocket client.

        :param base_client: the base canopy client
        """
        self._base_client = base_client
        self.websocket_server = self._base_client.websocket_server
        if self.websocket_server is None:
            # auto-generate websocket server hostname.
            # this will not work for a non-standard websocket server
            self.websocket_server = self._base_client.api_server.replace('api.', 'api-ws.') \
                .replace('api-gateway.', 'api-ws.') \
                .replace('https://', 'wss://') \
                .replace('http://', 'ws://')

    async def get(
            self,
            path: str,
            params: Dict = None,
            headers: Dict = None,
            timeout: int = 60
    ) -> CanopyResponse:
        """
        Make a GET Request to Canopy API.

        :param int timeout: the timeout for the response
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :return: json response as a dictionary
        """
        return await self._do_request('GET', path, params, headers, timeout)

    @property
    def authorized_websocket_server(self) -> str:
        """
        Get a websocket server URI.

        :return: the authorized websocket server URI
        """
        params = {'token': self._base_client.token}
        url_parts = list(urlparse(self.websocket_server))
        query = dict(parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urlencode(query)
        self.websocket_server = urlunparse(url_parts)
        return self.websocket_server

    @asynccontextmanager
    async def get_connection(self) -> WebSocketClientProtocol:
        """
        Get a websocket connection.

        :return: An authenticated instance of :class:`~websockets.client.WebSocketClientProtocol`.
        """
        ws_connection = await websockets.connect(self.authorized_websocket_server)
        await ws_connection.send(json.dumps({
            'action': 'getIdentity'
        }))
        response = json.loads(await ws_connection.recv())
        _connection_id = response['connectionId']
        _ws_connection = ws_connection
        try:
            yield _ws_connection, _connection_id
        finally:
            await _ws_connection.close()

    async def wait_for_response(self, w, request_id):
        """
        Wait for a response pertaining to the request ID.

        :param w:
        :param request_id:
        :return:
        """
        ws_response_request_id = None
        while request_id != ws_response_request_id:
            ws_raw_response = json.loads(await w.recv())
            ws_response_request_id = ws_raw_response.get('requestId')
            if ws_raw_response.get('status') == 'ok':
                if ws_raw_response.get('type') == 'completion_marker':
                    res = self._base_client.session.get('/api/ws', params={
                        'request_id': ws_response_request_id
                    })

                    if not res.ok:
                        raise CanopyAPIException('Failed to make a ws request.', res)

                    ws_raw_response = res.json()
                    if ws_raw_response.get('status') != 'ok':
                        return WebsocketResponse(status_code=ws_raw_response.get('code', 0), response=ws_raw_response)
                return WebsocketResponse(status_code=200, response=ws_raw_response)
            return WebsocketResponse(status_code=ws_raw_response.get('code', 0), response=ws_raw_response)

    async def _do_request(
            self,
            method: str,
            path: str,
            params: Dict = None,
            headers: Dict = None,
            timeout: int = 60
    ):
        """
        Perform a request to the websocket proxy. Response will be received via websocket connection.

        :param str method: the HTTP method to call (GET/POST/PATCH/PUT/DELETE)
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :param int timeout: the timeout for the response
        :return: json response as a dictionary
        """
        if params is None:
            params = {}
        if headers is None:
            headers = {}

        headers.update({
            'x-auth-username': self._base_client.session.headers.get('x-auth-username'),
            'x-app-id': self._base_client.session.headers.get('x-app-id'),
            'user-agent': self._base_client.session.headers.get('user-agent'),
        })

        self._base_client.ensure_session()

        if path.startswith('/'):
            path = path.lstrip('/')

        async with self.get_connection() as (ws, connection_id):
            res = self._base_client.session.post('/api/ws', json={
                'connectionId': connection_id,
                'request': {
                    'method': method,
                    'path': '/api/v1/' + path,
                    'queryParams': params,
                    'headers': headers,
                }
            })
            try:
                res = await asyncio.wait_for(self.wait_for_response(ws, res.json()['requestId']), timeout=timeout)
            except asyncio.TimeoutError:
                raise CanopyAPIException('Timed-out waiting for request.')
        if not res.ok:
            raise CanopyAPIException('Failed to make a ws request.', res)
        json_res = res.json()
        return json_res.get('payload', json_res)

    #
    # Synchronous-wrappers around the async methods
    #
    def get_sync(
            self,
            path: str,
            params: Dict = None,
            headers: Dict = None,
            timeout: int = 60
    ) -> CanopyResponse:
        """
        Make a GET Request to Canopy API.

        :param int timeout: the timeout for the response
        :param str path: the endpoint to call
        :param dict params: the query parameters to pass
        :param dict headers: the extra headers to set
        :return: json response as a dictionary
        """
        return asyncio.get_event_loop().run_until_complete(self.get(path, params, headers, timeout))
