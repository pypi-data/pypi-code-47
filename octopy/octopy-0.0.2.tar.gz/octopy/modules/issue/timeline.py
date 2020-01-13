from octopy import request, model


class Timeline:

    """
    Official GITHUB documentation: https://developer.github.com/v3/issues/timeline/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Issue-Timeline.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.mockingbird-preview"

    def all(self, owner, repo, issue_number, page=1):
        """
        Returns all events for an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg page: from which page events to be returned, default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/timeline?page={page}"
        items = [
            model.create_class("Issue", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items
