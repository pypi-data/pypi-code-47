from biscuit.api import API
from biscuit.middleware import Middleware

APP = API()


class CustomMiddleware(Middleware):
    def process_request(self, request):
        print("Processing request", request.url)

    def process_response(self, request, response):
        print("Processing response", request.url)


APP.add_middleware(CustomMiddleware)


def custom_exc_handler(request, response, exception):
    response.text = str(exception)


APP.add_exception_handler(custom_exc_handler)


@APP.route("/home", methods=["get"])
def home(request, response):
    response.text = "Hi from home"


@APP.route("/about")
def about(request, response):
    response.text = "Hi from about"


@APP.route("/hello/{name}")
def welcome(request, response, name):
    response.text = f"hi {name}"


@APP.route("/article")
class ArticleView:
    def get(self, request, response):
        response.text = "Article GET"

    def post(self, request, response):
        response.text = "Article POST"


@APP.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("Won't happen")
