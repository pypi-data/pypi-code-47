"""Main module for pact_state_provider package."""
import http.server
import importlib
import json
import logging
import socketserver
from typing import Callable, Optional

import click

INVALID_CHARS = [' ', ',', ';', '{', '}', '(', ')', '\n', '\t', '=']
TRANS_TABLE = str.maketrans({k: '_' for k in INVALID_CHARS})


def import_state_func(base_module: str, state: str) -> Optional[Callable]:
    """Translate the state name to a function name and get it from the base module."""
    logging.debug(f'Importing {base_module}')
    try:
        pkg = importlib.import_module(base_module)
        func_name = state.lower().translate(TRANS_TABLE)
        logging.debug(f'Getting function "{func_name}"')
        func = getattr(pkg, func_name, None)
    except ModuleNotFoundError:
        logging.error(f'Could not import base module "{base_module}"')
        return None
    return func


class StateProviderHandler(http.server.SimpleHTTPRequestHandler):
    """Handler to translate the request into a function and call it."""

    def __init__(self, request, client_address, server):
        """Store the servers base module for convenience."""
        self.base_module = server.base_module
        super().__init__(request, client_address, server)

    def do_POST(self):
        """Call the imported function based on the input dict."""
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data_string)
        consumer = data['consumer']
        state = data['state']

        state_func = import_state_func(self.base_module, state)
        if state_func is None:
            logging.debug(f'No function "{state}" found in {self.base_module}. Ignoring.')
        else:
            logging.debug(f'Calling provider')
            state_func(consumer)

        self.send_response(200)
        self.end_headers()


class StateProviderServer(socketserver.TCPServer):
    """TCPServer extended with the base module to load state providers from."""

    def __init__(self, server_address, bind_and_activate=True, base_module=''):
        """Store the provided base module on top of the TCPServer initialization."""
        # pytype: disable=wrong-arg-types
        super().__init__(
            server_address,
            StateProviderHandler,
            bind_and_activate
        )
        # pytype: enable=wrong-arg-types
        self.base_module = base_module


@click.command()
@click.option(
    '--base-module',
    default='pact_state_provider.example',
    help='Module containing the state providers.'
)
@click.option('--host', default='127.0.0.1', help='Host for the endpoint. Default: 127.0.0.1')
@click.option('--port', default=1235, help='Port for the endpoint. Default: 1235')
@click.option(
    '--log-level',
    default='INFO',
    help='Log Level Name (DEBUG, INFO, ...). Default: INFO'
)
def pact_state_provider(base_module, host, port, log_level):
    """Start the state provider server on the specified host and port."""
    logging.getLogger().setLevel(logging.getLevelName(log_level))
    httpd = StateProviderServer((host, port), base_module=base_module)
    logging.info(
        f'Serving at {host}:{port}. Using module {base_module}'
    )

    httpd.serve_forever()
    httpd.shutdown()


if __name__ == '__main__':
    pact_state_provider()
