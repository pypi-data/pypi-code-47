from flask import current_app, request
from flask_middleware_jwt import middleware_request
from flask_socketio import emit
import json
import logging
from functools import wraps

logger = logging.getLogger(__name__)

CONFIG_DEFAULTS = {
    'MIDDLEWARE_URL_IDENTITY': '0.0.0.0:5000',
    'MIDDLEWARE_VERIFY_ENDPOINT': '/token/verify',
    'MIDDLEWARE_BEARER': True,
    'MIDDLEWARE_VERIFY_HTTP_VERB': 'GET',
    'JWT_SECRET': 'YOUR_SECRET_KEY',
    'JWT_ALGORITHMS': ['HS256'],
    'EMIT_NAME': 'my_response'
}


def middleware_jwt_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        validate_key()

        if current_app.config.get('MIDDLEWARE_BEARER'):
            validate_bearer()            

        response = middleware_request(request.headers["Authorization"])

        if type(response) == tuple:
            emit(current_app.config.get("EMIT_NAME"),response)
            return None
        response_content = json.loads(response.content)

        if response.status_code != 200:
            emit(current_app.config.get("EMIT_NAME"),{'content': (response_content), 'status_code': response.status_code})
            return None
            
        return f(*args, **kwargs)
    return decorator


def validate_key():
    if "Authorization" not in list(request.headers.keys()):
        emit(current_app.config.get("EMIT_NAME"),{'message': 'Authorization not found', 'status_code': 404})
        return None

def validate_bearer():
    if 'Bearer ' not in request.headers["Authorization"]:
        emit(current_app.config.get("EMIT_NAME"),{'message': 'Authorization no serialized' , 'status_code': 404})
        return None



class Middleware(object):
    def __init__(self, app):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        for k, v in CONFIG_DEFAULTS.items():
            if k not in app.config.keys():
                app.config.setdefault(k, v)
