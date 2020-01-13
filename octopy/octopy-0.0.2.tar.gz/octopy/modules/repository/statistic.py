from octopy import request, model


class Statistic:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/statistics/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Statistic
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def contributors(self):
        """
        Returns all contributors with additions, deletions, and commit counts.
        """
        url = f"{self._url}/repos/{owner}/{repo}/stats/contributors"
        items = [
            model.create_class("Contributor", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def commit_activity(self, owner, repo):
        """
        Returns the last year of commit activity data.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/stats/commit_activity"
        items = [
            model.create_class("Activity", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def additions_and_deletions(self, owner, repo):
        """
        Returns the number of additions and deletions per week.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/stats/code_frequency"
        items = [
            model.create_class("AdditionsAndDeletions", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def repository(self, owner, repo):
        """
        Returns the weekly commit count for a repository.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/stats/participation"
        return model.create_class(
            "WeeklyCommitCount", request.get(url, headers=self._headers)
        )
