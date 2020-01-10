from octopy import request, model


class Repository:

    """
    Official GITHUB documentation: https://developer.github.com/v3/interactions/repos/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Interaction-Repository.md
    """

    def __init__(self, url, headers):

        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.sombra-preview"

    def restrictions(self, owner, repo):
        """
        Shows the group of users which can interact with the given repository,
        and when that expires.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._headers}/repos/{owner}/{repo}/interaction-limits"
        return model.create_class(
            "InteractionLimit", request.get(url, headers=self._headers)
        )

    def update(self, owner, repo, **kwargs):
        """
        Updates/Creates restrict interactions to a group of Github users.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg limit: [required] specifies the group of users who can comment,
            open issues, or create a pull request. 
        """
        url = f"{self._headers}/repos/{owner}/{repo}/interaction-limits"
        return model.create_class(
            "Repository", request.put(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo):
        """
        Removes all interaction restrictions to a given repository.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._headers}/repos/{owner}/{repo}/interaction-limits"
        return model.create_class("Status", request.delete(url, headers=self._headers))
