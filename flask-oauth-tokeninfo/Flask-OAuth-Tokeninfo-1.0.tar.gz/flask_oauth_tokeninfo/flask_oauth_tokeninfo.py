import json
from functools import wraps

import flask
import requests
from flask import _request_ctx_stack, request, jsonify, current_app
from requests.auth import HTTPBasicAuth
from werkzeug.local import LocalProxy

current_user = LocalProxy(lambda: get_user())


class ValidationException(Exception):
    pass


def get_user():
    return getattr(_request_ctx_stack.top, 'user', None)


def get_roles():
    resource_access = current_user.get("resource_access")

    if resource_access is None:
        return []

    client_dict = resource_access.get(current_app.config.get('AUTH_CLIENT_ID'))

    if client_dict is None:
        return []

    return client_dict.get("roles", [])


def get_scopes():
    scope = current_user.get("scope")

    if scope is None:
        return []

    return scope.split(" ")


def has_role(role):
    return role in get_roles()


def has_role_one_of(list):
    for expected in list:
        if expected in get_roles():
            return True
    return False


def has_role_all_of(list):
    for expected in list:
        if expected not in get_roles():
            return False
    return True


def has_scope(scope):
    return scope in get_scopes()


def has_scope_one_of(list):
    for expected in list:
        if expected in get_scopes():
            return True
    return False


def has_scope_all_of(list):
    for expected in list:
        if expected not in get_scopes():
            return False
    return True


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

    def check_token(self, view_func):
        @wraps(view_func)
        def decorated(*args, **kwargs):
            ctx = _request_ctx_stack.top

            tokeninfo_endpoint = current_app.config.get('AUTH_TOKENINFO_ENDPOINT')
            client_id = current_app.config.get('AUTH_CLIENT_ID')
            client_secret = current_app.config.get('AUTH_CLIENT_SECRET')

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
