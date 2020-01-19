from .lambda_function import LambdaFunction
import json


class APIFunction(LambdaFunction):
    def __init__(self, event, context):
        print("API init.")
        print(event)

    def __call__(self, event, context):
        self.__init__()

        # Get the calling method and route appropriately.
        method = event["httpMethod"].lower()

        # TODO: Should use a more elegent method of routing here.
        if method == "post":
            response = self.post(event)

        elif method == "get":
            response = self.get(event)

        elif method == "put":
            response = self.put(event)

        else:
            raise Exception(f"Triggered with unexpected HTTP method {method}.")

        return response

    def create_return(self, status_code=200, body=None):
        return_obj = {"statusCode": status_code}
        if body:
            return_obj["body"] = json.dumps(body)

    def get_methods(self):
        methods = []
        # Check post method.
        post = getattr(self, "post", None)
        if callable(post):
            methods.append("post")

        # Check get method.
        get = getattr(self, "get", None)
        if callable(get):
            methods.append("get")

        # Check put method.
        put = getattr(self, "put", None)
        if callable(put):
            methods.append("put")

        return methods
