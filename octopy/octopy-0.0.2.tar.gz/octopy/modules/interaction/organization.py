from octopy import request, model


class Organization:

    """
    Official GITHUB documentation: https://developer.github.com/v3/interactions/orgs/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Interaction-Organization.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.sombra-preview"

    def restrictions(self, org):
        """
        Shows the group of users which can interact with the given organization,
        and when that interacton expires.

        :param org: org's name
        """
        url = f"{self._url}/orgs/{org}/interaction-limits"
        return model.create_class(
            "IteractionLimit", request.get(url, headers=self._headers)
        )

    def update(self, org, **kwargs):
        """
        Restricts interactions to certain Github users.

        :param org: org's name
        :kwarg limit: [required] specifies the group of users
            which can comment, open issues, or create pull resuqest.
        """
        url = f"{self._url}/orgs/{org}/interaction-limits"
        return model.create_class(
            "Organization", request.put(url, headers=self._headers, params=kwargs)
        )

    def remove(self, org):
        """
        Removes all interaction restrictions from public repositories.

        :param org: org's name
        """
        url = f"{self._url}/orgs/{org}/interaction-limits"
        return model.create_class("Status", request.delete(url, headers=self._headers))
