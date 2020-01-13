from octopy import request, model


class Traffic:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/traffic/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Traffic
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def refferers(self, owner, repo):
        """
        Returns the top 10 refferers over the last 14 days.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/traffic/popular/referrers"
        items = [
            model.create_class("Refferer", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def paths(self, owner, repo):
        """
        Returns top 10 popular contents of the last 14 days.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/traffic/popular/paths"
        items = [
            model.create_class("Path", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def views(self, owner, repo, **kwargs):
        """
        Returns the total number of views and breakdown per day or week for the
        last 14 days.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg per: must be one of `day`, `week`; default: `day`
        """
        url = f"{self._url}/repos/{owner}/{repo}/traffic/views"
        items = [
            model.create_class("View", item)
            for item in request.get(url, headers=self._headers, params=kwargs)["views"]
        ]
        return items

    def clones(self, owner, repo, **kwargs):
        """
        Returns all number of clones.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg per: must be one of `day`, or `week`; default: `day`
        """
        url = f"{self._url}/repos/{owner}/{repo}/traffic/clones"
        items = [
            model.create_class("Clone", item)
            for item in request.get(url, headers=self._headers, params=kwargs)["clones"]
        ]
        return items
