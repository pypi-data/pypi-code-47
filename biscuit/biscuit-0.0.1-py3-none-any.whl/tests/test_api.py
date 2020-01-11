from biscuit.api import API
import pytest
from biscuit.middleware import Middleware


APP = API()


class TestAPI:
    """Test API class"""

    def test_adding_route_handlers(self, mocker):
        """Should add a route handler"""
        test = APP.route("/test_route")

        test(mocker)

        assert APP.routes["/test_route"]

    def test_route_duplicate_throws_exception(self, api):
        @api.route("/duplicate")
        def duplicate(request, response):
            response.text = "test"

        with pytest.raises(AssertionError):

            @api.route("/duplicate")
            def duplicate2(request, response):
                response.text = "test"

    def test_custom_exception_handler(self, api, client):
        def on_exception(request, response, exc):
            response.text = "AttributeErrorHappened"

        api.add_exception_handler(on_exception)

        @api.route("/")
        def index(request, response):
            raise AttributeError()

        resp = client.get("http://testserver/")
        assert resp.text == "AttributeErrorHappened"

    def test_middleware(self, api, client):
        process_request_called = False
        process_response_called = False

        class CallMiddlewareMethods(Middleware):
            def __init__(self, app):
                super().__init__(app)

            def process_request(self, request):
                nonlocal process_request_called
                process_request_called = True

            def process_response(self, request, response):
                nonlocal process_response_called
                process_response_called = True

        api.add_middleware(CallMiddlewareMethods)

        @api.route("/")
        def index(request, response):
            response.text = "middleware"

        resp = client.get("http://testserver/")
        assert resp.text == "middleware"
        assert process_response_called is True
        assert process_request_called is True

    def test_allowed_methods(self, client, api):
        @api.route("/test", methods=["post"])
        def index(request, response):
            response.text = "Testing"

        with pytest.raises(AttributeError):
            client.get("http://testserver/test")

        assert client.post("http://testserver/test").text == "Testing"
