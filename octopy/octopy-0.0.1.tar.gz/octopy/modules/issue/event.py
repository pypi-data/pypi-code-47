from octopy import request, model


class Event:

    """
    Official GITHUB documentation: https://developer.github.com/v3/issues/events/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Issue-Event.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, issue_number, page=1):
        """
        Returns all events for an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg page: from which page events to be returned
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/events?page={page}"
        )
        items = [
            model.create_class("Event", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def repository(self, owner, repo, page=1):
        """
        Returns all events of a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page events to be returned
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/events?page={page}"
        items = [
            model.create_class("RepoEvent", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, owner, repo, event_id):
        """
        Returns a single evnet.

        :param owner: owner's name
        :param repo: repo's name
        :param event_id: event's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/events/{event_id}"
        return model.create_class("Event", request.get(url, headers=self._headers))
