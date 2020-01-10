from nonsensepy import NonsensePyGen as np
import requests

from .error import OctopyException


class OctopyAuth:
    AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
    ACCESS_TOKEN = "https://github.com/login/oauth/access_token"

    def __init__(self, **kwargs):
        self.client_id = kwargs.get("client_id", "")
        self.client_secret = kwargs.get("client_secret", "")
        self.state = kwargs.get("state", np.strrandom(max=20))
        self.scope = kwargs.get("scope", [])
        self.redirect_uri = kwargs.get("redirect_uri", "http://localhost")

    def authorize(self, **kwargs):
        if not kwargs.get("state"):
            state = self.state

        scope = kwargs.get("scope", self.scope)
        scope = ",".join(scope) if type(scope) is list else scope
        allow_signup = "true" if kwargs.get("allow_signup") else "false"

        params = {
            "client_id": kwargs.get("client_id", self.client_id),
            "redirect_uri": kwargs.get("redirect_uri", self.redirect_uri),
            "scope": scope,
            "allow_signup": allow_signup,
            "state": kwargs.get("state", self.state),
        }

        if kwargs.get("login"):
            params["login"] = kwargs["login"]

        url = self.AUTHORIZE_URL + "?{}".format(
            "&".join(["{}={}".format(key, value) for key, value in params.items()])
        )

        return url

    def authentication_token(self, **kwargs):
        url = kwargs.get("url")

        code = kwargs.get("code")
        if url:
            code = url.split("?")[1].split("&")[0].split("=")[1]

        params = {
            "client_id": kwargs.get("client_id", self.client_id),
            "client_secret": kwargs.get("client_secret", self.client_secret),
            "redirect_uri": kwargs.get("redirect_uri", self.redirect_uri),
            "state": kwargs.get("state", self.state),
            "code": code,
        }

        response = requests.post(self.ACCESS_TOKEN, data=params)

        if response.status_code != requests.codes.ok:
            raise OctopyException(
                "Error with status code {} occurred.".format(response.status_code)
            )

        token = response.text.split("&")[0].split("=")[1]
        return token
