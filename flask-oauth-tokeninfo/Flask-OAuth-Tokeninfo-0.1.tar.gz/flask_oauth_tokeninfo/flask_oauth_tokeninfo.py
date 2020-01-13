import json
import sqlite3
from functools import wraps

import requests
from flask import _request_ctx_stack, request
from requests.auth import HTTPBasicAuth


class OauthTokenInfo(object):
    def __init__(self, app):
        self.app = app
        if app is not None:
            self.init_app(app)

        self.tokeninfo_endpoint = None
        self.client_id = None
        self.client_secret = None

    def init_app(self, app):
        app.config.setdefault('AUTH_TOKENINFO_ENDPOINT', None)
        app.config.setdefault('AUTH_CLIENT_ID', None)
        app.config.setdefault('AUTH_CLIENT_SECRET', None)

        tokeninfo_endpoint = app.config.get('AUTH_TOKENINFO_ENDPOINT')
        client_id = app.config.get('AUTH_CLIENT_ID')
        client_secret = app.config.get('AUTH_CLIENT_SECRET')

        if tokeninfo_endpoint is None:
            raise Exception("Tokeninfo endpoint is required")

        if client_id is None:
            raise Exception("Client id is required")

        if client_secret is None:
            raise Exception("Client secret is required")

        self.tokeninfo_endpoint = tokeninfo_endpoint
        self.client_id = client_id
        self.client_secret = client_secret

    def require_login(self, view_func):
        @wraps(view_func)
        def decorated(*args, **kwargs):
            ctx = _request_ctx_stack.top

            header = request.headers.get("Authorization")
            token = header.replace("Bearer ", "")

            response = requests.post(self.tokeninfo_endpoint, auth=HTTPBasicAuth(self.client_id, self.client_secret),
                                     data={"token": token})

            tokeninfo = json.loads(response.text)

            ctx.user = tokeninfo

            return view_func(*args, **kwargs)

        return decorated

    def connection(self):
        ctx = _request_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sqlite3_db'):
                ctx.sqlite3_db = self.connect()
            return ctx.sqlite3_db
