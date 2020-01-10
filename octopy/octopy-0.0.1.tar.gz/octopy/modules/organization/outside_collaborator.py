from octopy import request, model


class OutsideCollaborator:

    """
    Official GITHUB documentation: https://developer.github.com/v3/orgs/outside_collaborators/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Organizations-OutsideCollaborators.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, org, page=1, **kwargs):
        """
        Returns all users, who are outside collaborators for an org.

        :param org: org's name
        :kwarg page: from which page, users to be returned, default: 1
        :kwarg filter: filter's users. 
            Can be `2fa_disabled`, or `all`(default)
        """
        url = f"{self._url}/orgs/{org}/outside_collaborators?page={page}"
        items = [
            model.create_class("OutsideCollaborator", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def remove(self, org, username):
        """
        Removes an outside collaborator.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/outside_collaborators/{username}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def create(self, org, username):
        """
        Makes a user to an outside collaborator.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/outside_collaborators/{username}"
        return model.create_class("Status", request.put(url, headers=self._headers))
