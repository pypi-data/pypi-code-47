from octopy import request, model


class Assignee:

    """
    Official GITHUB documentation: https://developer.github.com/v3/issues/assignees/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Issue-Assignee.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1):
        """
        Returns all assignees for issues in a repository.
        
        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page results to be returned,
            by default is set to 1.
        """
        url = f"{self._url}/repos/{owner}/{repo}/assignees?page={page}"
        items = [
            model.create_class("Asignee", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def check(self, owner, repo, assignee):
        """
        Checks if a user has permission to be assigned to an issue in a given repository.

        :param owner: owner's name
        :param repo: repo's name
        :param assignee: user's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/assignees/{assignee}"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def create(self, owner, repo, issue_number, **kwargs):
        """
        Adds up to 10 assignees to an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg assignees: list with usernames
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/assignees"
        return model.create_class(
            "Assignee", request.post(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, issue_number, **kwargs):
        """
        Removes one or more assignees from an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg assignees: list with usernames
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/assignees"
        return model.create_class(
            "Assignee", request.delete(url, headers=self._headers, params=kwargs)
        )
