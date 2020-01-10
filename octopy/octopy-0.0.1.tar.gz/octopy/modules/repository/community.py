from octopy import request, model


class Community:

    """
    Official GITHUB documentation: 
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def profile(self, owner, repo):
        """
        Returns community profile metrics.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/community/profile"
        return model.create_class(
            "CommunityProfile", request.get(url, headers=self._headers)
        )
