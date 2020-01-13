from octopy import request, model


class Starring:

    """
    Official documentation in Github: https://developer.github.com/v3/activity/starring/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/ActivityStarring.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1, when=False):
        """
        Returns a list with users, starring a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page users to be returned, by default is set to 1.
        :kwarg when: if set to true, will return information when a user was starred the repository.
        """
        headers = self._headers
        if when:
            headers = self._headers.copy()
            headers["Accept"] = "application/vnd.github.v3.star+json"

        url = f"{self._url}/repos/{owner}/{repo}/stargazers?page={page}"
        items = [
            model.create_class("Star", item)
            for item in request.get(url, headers=headers)
        ]
        return items

    def starred(self, username=None, page=1, when=False):
        """
        Returns a list with repositories, being starred by a user.

        :kwarg username: if given, will return repositories, starred by the given user.
                By default is set to none, which means that repositories returned are those
                starred by the authenticated user.
        :kwarg page: from which page repositories to be returned. By default is set to 1.
        :kwarg when: if set to true, will include information when the starring happen.
        """
        headers = self._headers
        if when:
            headers = self._headers.copy()
            headers["Accept"] = "application/vnd.github.v3.star+json"

        url = (
            f"{self._url}/users{f'/{username}' if username else ''}/starred?page={page}"
        )

        items = [
            model.create_class("Starred", item)
            for item in request.get(url, headers=headers)
        ]
        return items

    def am_i_starring(self, owner, repo):
        """
        Check if the authenticated user is starring a repo.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/user/starred/{owner}/{repo}"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def star(self, owner, repo):
        """
        Stars a repository.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/user/starred/{owner}/{repo}"
        return model.create_class("Status", request.put(url, headers=self._headers))

    def unstar(self, owner, repo):
        """
        Unstars a repository.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/user/starred/{owner}/{repo}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
