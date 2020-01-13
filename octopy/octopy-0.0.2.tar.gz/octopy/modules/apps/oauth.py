from octopy import request, model


class OAuth:

    """
    Official documentation in Github: https://developer.github.com/v3/apps/oauth_applications/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/App-OAuth.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.doctor-strange-preview+json"

    def check(self, client_id, **kwargs):
        """
        Checks a token.

        :param client_id: client's id
        :kwarg access_token: token for check
        """
        url = f"{self._url}/applications/{client_id}/token"
        return model.create_class(
            "AccessToken", request.post(url, headers=self._headers, params=kwargs)
        )

    def reset(self, client_id, **kwargs):
        """
        Resets an access token.

        :param client_id: client's id
        :kwarg access_token: an access token
        """
        url = f"{self._url}/applications/{client_id}/token"
        return model.create_class(
            "AccessToken", request.post(url, headers=self._headers, params=kwargs)
        )

    def remove(self, client_id, **kwargs):
        """
        Deletes a token.

        :param client_id: client's id
        :kwarg access_token: an access token
        """
        url = f"{self._url}/applications/{client_id}/token"
        return model.create_class(
            "Status", request.delete(url, headers=self._headers, params=kwargs)
        )

    def remove_authorization(self, client_id, **kwargs):
        """
        Deletes an authorization token.

        :param client_id: client's id
        :param access_token: an access token.
        """
        url = f"{self._url}/applications/{client_id}/grant"
        return model.create_class(
            "Status", request.delete(url, headers=self._headers, params=kwargs)
        )
