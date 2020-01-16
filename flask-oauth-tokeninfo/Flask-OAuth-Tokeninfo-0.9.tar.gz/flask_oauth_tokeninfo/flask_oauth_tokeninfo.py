import json
from functools import wraps

import flask
import requests
from flask import _request_ctx_stack, request, jsonify, current_app
from requests.auth import HTTPBasicAuth
from werkzeug.local import LocalProxy

current_user = LocalProxy(lambda: _get_user())


class ValidationException(Exception):
    pass


def _get_user():
    return getattr(_request_ctx_stack.top, 'user', None)


class OAuthTokenInfo(object):
    def __init__(self, app):
        self.app = app
        if app is not None:
            self.init_app(app)

        self.tokeninfo_endpoint = None
        self.client_id = None
        self.client_secret = None

    def init_app(self, app):
        tokeninfo_endpoint = app.config.get('AUTH_TOKENINFO_ENDPOINT')
        client_id = app.config.get('AUTH_CLIENT_ID')
        client_secret = app.config.get('AUTH_CLIENT_SECRET')

        if tokeninfo_endpoint is None:
            raise ValidationException("AUTH_TOKENINFO_ENDPOINT config is required")

        if client_id is None:
            raise ValidationException("AUTH_CLIENT_ID config is required")

        if client_secret is None:
            raise ValidationException("AUTH_CLIENT_SECRET config is required")

        current_app.tokeninfo_endpoint = tokeninfo_endpoint
        current_app.client_id = client_id
        current_app.client_secret = client_secret

    def check_token(self, view_func):
        tokeninfo_endpoint = current_app.tokeninfo_endpoint
        client_id = current_app.client_id
        client_secret = current_app.client_secret

        @wraps(view_func)
        def decorated(*args, **kwargs):
            ctx = _request_ctx_stack.top

            header = request.headers.get("Authorization")

            if header is None:
                response = jsonify({'message': "Token is not given"})
                response.status_code = 403
                return flask.abort(response)

            token = header.replace("Bearer ", "")

            response = requests.post(tokeninfo_endpoint, auth=HTTPBasicAuth(client_id, client_secret),
                                     data={"token": token})

            tokeninfo = json.loads(response.text)

            if not tokeninfo["active"]:
                response = jsonify({'message': "Token is inactive"})
                response.status_code = 403
                return flask.abort(response)

            ctx.user = tokeninfo

            return view_func(*args, **kwargs)

        return decorated
