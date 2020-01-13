from octopy import request, model


class Status:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/statuses/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Status
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def create(self, owner, repo, sha, **kwargs):
        """
        Users with push access in a repository can create
        commit statuses for a given SHA.

        :param owner: owner's name
        :param repo: repo's name
        :param sha: 
        :kwarg state: [required] state of the status
        :kwarg target_url: The target URL to associate with this status. 
            This URL will be linked from the GitHub UI to 
            allow users to easily see the source of the status.
            For example, if your continuous integration system 
            is posting build status, you would want to 
            provide the deep link for the build output 
            for this specific SHA:
            http://ci.example.com/user/repo/build/sha
        :kwarg description:
        :kwarg context:
        """
        url = f"{self._url}/repos/{owner}/{repo}/statuses/{sha}"
        return model.create_class(
            "Status", request.post(url, headers=self._headers, params=kwargs)
        )

    def all(self, owner, repo, ref, page=1):
        """
        Returns statuses for a specific ref.

        :param owner: owner's name
        :param repo: repo's name
        :param ref:
        :kwarg page: from which page statuses to be returned; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/commits/{ref}/statuses?page={page}"
        items = [
            model.create_class("Status", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def combined(self, owner, repo, ref):
        """
        Returns combinded status for a specific ref.

        :param owner: owner's name
        :param repo: repo's name
        :param ref: 
        """
        url = f"{self._url}/repos/{owner}/{repo}/commits/{ref}/status"
        return model.create_class("Combined", request.get(url, headers=self._headers))
