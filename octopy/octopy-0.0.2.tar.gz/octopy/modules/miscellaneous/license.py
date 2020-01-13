from octopy import request, model


class License:

    """
    Official GITHUB documentation: https://developer.github.com/v3/licenses/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Miscellaneous-License.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self):
        """
        Returns commonly used licenses.
        """
        url = f"{self._url}/licenses"
        items = [
            model.create_class("License", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, name):
        """
        Returns an individual license.

        :param name: license's name
        """
        url = f"{self._url}/licenses/{name}"
        return model.create_class("License", request.get(url, headers=self._headers))

    def repository(self, owner, repo):
        """
        Returns the license of a repo.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/license"
        return model.create_class(
            "RepoLicense", request.get(url, headers=self._headers)
        )
