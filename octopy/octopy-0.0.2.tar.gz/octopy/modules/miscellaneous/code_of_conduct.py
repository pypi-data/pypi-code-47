from octopy import request, model


class CodeOfConduct:

    """
    Official GITHUB documentation: https://developer.github.com/v3/codes_of_conduct/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Miscellaneous-CodeOfConduct.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.scarlet-witch-preview+json"

    def all(self):
        """
        Returns all codes of conduct.
        """
        url = f"{self._url}/codes_of_conduct"
        items = [
            model.create_class("CodeOfConduct", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, key):
        """
        Returns an individual code of conduct.

        :param key: code of conduct's key
        """
        url = f"{self._url}/code_of_conduct/{key}"
        return model.create_class(
            "CodeOfConduct", request.get(url, headers=self._headers)
        )

    def repository(self, owner, repo, content=False):
        """
        Returns a repository's code of conduct.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg content: if set to true, it will return the content of the code of conduct
        """
        url = f"{self._url}/repos/{owner}/{repo}{'/community/code_of_conduct' if content else ''}"
        return model.create_class(
            "CodeOfConduct", request.get(url, headers=self._headers)
        )
