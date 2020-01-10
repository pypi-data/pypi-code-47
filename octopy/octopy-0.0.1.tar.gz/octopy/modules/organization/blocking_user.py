from octopy import request, model


class BlockingUser:

    """
    Official GITHUB documentation: https://developer.github.com/v3/orgs/blocking/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Organizations-BlockingUser.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers[
            "Accept"
        ] = "application/vnd.github.giant-sentry-fist-preview+json"

    def all(self, org):
        """
        Returns all users blocked by an organization.

        :param org: org's name
        """
        url = f"{self._url}/orgs/{org}/blocks"
        items = [
            model.create_class("BlockedUser", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def blocked(self, org, username):
        """
        Checks if a user is blocked by an organization.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/blocks/{username}"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def block(self, org, username):
        """
        Blocks a user.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/blocks/{username}"
        return model.create_class("Status", request.put(url, headers=self._headers))

    def unblock(self, org, username):
        """
        Unblocks a user.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/blocks/{username}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
