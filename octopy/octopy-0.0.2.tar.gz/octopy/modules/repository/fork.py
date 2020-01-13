from octopy import request, model


class Fork:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/forks/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Fork
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1, **kwargs):
        """
        Returns all forks for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page forks to be returned
        :kwarg sort: can be `newest`, `oldest`, or `stargazers`; default: `newest`
        """
        url = f"{self._url}/repos/{owner}/{repo}/forks?page={page}"
        items = [
            model.create_class("Fork", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def create(self, owner, repo, **kwargs):
        """
        Creates a fork.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg organization: org's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/forks"
        return model.create_class(
            "Fork", request.post(url, headers=self._headers, params=kwargs)
        )
