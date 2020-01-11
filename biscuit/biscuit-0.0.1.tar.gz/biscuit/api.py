import inspect
from parse import parse
from webob import Request, Response
from requests import Session as ReqSession
from wsgiadapter import WSGIAdapter as ReqWSGIAdapter

from .middleware import Middleware

DEFAULT_METHODS = ["get", "post", "put", "patch", "delete", "options"]


class API:
    """API for instantiating necessary PEP-333 call"""

    def __init__(self):
        self.routes = {}
        self.exception_handler = None
        self.middleware = Middleware(self)

    def __call__(self, environ, start_response):
        """PEP-333(3) use middleware as entrypoint"""
        return self.middleware(environ, start_response)

    def handle_request(self, request):
        """Handle a request and return correct path handler"""
        response = Response()

        handler_data, kwargs = self.select_handler(request.path)

        try:
            if handler_data is not None:
                handler = handler_data["handler"]
                allowed_methods = handler_data["allowed_methods"]
                if inspect.isclass(handler):
                    handler = getattr(handler(), request.method.lower(), None)
                    if handler is None:
                        raise AttributeError("Invalid method.", request.method)
                else:
                    if request.method.lower() not in allowed_methods:
                        raise AttributeError("Invalid method.", request.method)

                handler(request, response, **kwargs)
            else:
                self.default_response(response)
        except Exception as exc:
            if self.exception_handler is None:
                raise exc
            self.exception_handler(request, response, exc)

        return response

    def select_handler(self, req_path):
        """Select handler for request path"""
        for path, handler_data in self.routes.items():
            parse_result = parse(path, req_path)
            if parse_result is not None:
                return handler_data, parse_result.named

        return None, None

    def add_route(self, path, handler, allowed_methods):
        assert path not in self.routes, "Route already defined."

        if allowed_methods is None:
            allowed_methods = DEFAULT_METHODS
        self.routes[path] = {
            "handler": handler,
            "allowed_methods": allowed_methods,
        }

    def route(self, path, methods=None):
        """Handle routes"""

        def wrapper(handler):
            self.add_route(path, handler, methods)
            return handler

        return wrapper

    def default_response(self, response):
        """Return default response of 404 for paths not in self.routes"""
        response.status_code = 404
        response.text = "handler not found"

    def add_exception_handler(self, exception_handler):
        """Add custom exception handling"""
        self.exception_handler = exception_handler

    def add_middleware(self, middleware):
        """Add middleware"""
        self.middleware.add(middleware)

    def test_session(self, base_url="http://testserver"):
        """Test session for sending requests to the app"""
        session = ReqSession()
        session.mount(prefix=base_url, adapter=ReqWSGIAdapter(self))
        return session
