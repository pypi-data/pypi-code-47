from webob import Request


class Middleware:
    """Custom middleware"""

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        """PEP 333 compliant entrypoint"""
        request = Request(environ)
        response = self.app.handle_request(request)
        return response(environ, start_response)

    def add(self, middleware):
        """Add middleware"""
        self.app = middleware(self.app)

    def process_request(self, request):
        """Process the request"""
        pass

    def process_response(self, request, response):
        """Process the response"""
        pass

    def handle_request(self, request):
        """Handle a request"""
        self.process_request(request)
        response = self.app.handle_request(request)
        self.process_response(request, response)
        return response
