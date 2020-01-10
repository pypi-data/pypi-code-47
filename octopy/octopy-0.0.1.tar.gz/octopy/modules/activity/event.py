from octopy import request, model


class Event:

    """
    Official documentation in Github: https://developer.github.com/v3/activity/events/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/ActivityEvents.md
    """

    def __init__(self, url, headers, **kwargs):
        self._url = url
        self._headers = headers

    def all(self, page=1):
        """
        Returns all public events in Github.

        :kwargs page: Returns results from the given page. By default is set to 1.
        """
        url = f"{self._url}/events?page={page}"
        events = [
            model.create_class("Event", event)
            for event in request.get(url, headers=self._headers)
        ]
        return events

    def repository(self, owner, repo, page=1):
        """
        Returns all events of an owner's repo.

        :param owner: Name of the owner
        :param repo: Name of the repository
        :kwargs page: Returns results from the given page. By default is set to 1.
        """
        url = f"{self._url}/repos/{owner}/{repo}/events?{page}"
        response = request.get(url, headers=self._headers)
        items = [model.create_class("RepositoryEvent", item) for item in response]
        return items

    def issue(self, owner, repo, page=1):
        """
        Returns all issue events of an owner's repo.

        :param owner: Name of the owner
        :param repo: Name of the repository
        :kwargs page: Returns results from the given page. By default is set to 1.
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/events?page={page}"
        items = [
            model.create_class("IssueEvent", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def network(self, owner, repo, page=1):
        """
        Returns all network events of an owner's repo.

        :param owner: Name of the owner
        :param repo: Name of the repository
        :kwargs page: Returns results from the given page. By default is set to 1.
        """
        url = f"{self._url}/networks/{owner}/{repo}/events?page={page}"
        items = [
            model.create_class("NetworkEvent", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def organization(self, org, page=1):
        """
        Returns all events connected with an organization.

        :param org: Name of the organization.
        :kwargs page: Returns results from the given page. By default is set to 1.
        """
        url = f"{self._url}/orgs/{org}/events?page={page}"
        items = [
            model.create_class("OrgEvent", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def received(self, username, public=False, page=1):
        """
        Returns all events received by a user with given username.

        :param username: Name of the user
        :kwarg public: By default if you are authenticated and want to get your
            events, you will see all public & private events, if you select public to True,
            it will return only your public events. By default is set to False.
        :kwargs page: Returns results from the given page. By default is set to 1.
        """
        url = f"{self._url}/users/{username}/received_events{'/public' if public else ''}?page={page}"
        items = [
            model.create_class("ReceivedEvent", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def performed(self, username, public=False, page=1):
        """
        Returns all events performed by a user with given username.

        :param username: Name of the user.
        :kwarg public: By default if you are authenticated and want to see your
            events, you will see all public & private events, if you select public to True,
            it will return only your public events. By default is set to False.
        :kwargs page: Returns results from the given page. By default is set to 1.
        """
        url = f"{self._url}/users/{username}/events{'/public' if public else ''}?page={page}"
        items = [
            model.create_class("PerformedEvent", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def user_dashboard(self, username, org, page=1):
        """
        Returns all events from the user's organization dashboard.
        Only authenticated users can call this method.

        :param username: Name of the user.
        :param org: Name of the organization.
        :kwargs page: Returns results from the given page. By default is set to 1.
        """
        url = f"{self._url}/users/{username}/events/orgs/{org}?page={page}"
        items = [
            model.create_class("OrgEvent", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items
