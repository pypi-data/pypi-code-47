from octopy import request, model


class BlockingUser:

    """
    Official GITHUB documentation: 
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Users.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers[
            "Accept"
        ] = "application/vnd.github.giant-sentry-fist-preview+json"

    def all(self):
        """
        Returns all blocked by currently authenticated user, users.
        """
        url = f"{self._url}/user/blocks"
        items = [
            model.create_class("User", item)
            for item in request.get(url, headers=self._headers)[0]
        ]
        return items

    def blocked(self, username):
        """
        Checks if a user is blocked by currently authenticated user.

        :param username: user's name
        """
        url = f"{self._url}/user/blocks/{username}"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def block(self, username):
        """
        Blocks a user.

        :param username: user's name
        """
        url = f"{self._url}/user/blocks/{username}"
        return model.create_class("Status", request.put(url, headers=self._headers))

    def unblock(self, username):
        """
        Unblocks a user.

        :param username: user's name
        """
        url = f"{self._url}/user/blocks/{username}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
