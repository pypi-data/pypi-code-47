from octopy import request, model


class Watch:

    """
    Official documentation in Github: https://developer.github.com/v3/activity/watching/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/ActivityWatching.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1):
        """
        Returns a list with watchers.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page, watchers to be returned. By default is set to 1.
        """
        url = f"{self._url}/repos/{owner}/{repo}/subscribers?page={page}"
        items = [
            model.create_class("Subscriber", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def repository(self, username=None, page=1):
        """
        Returns a list with repositories being watched by a user.

        :kwarg username: if given, will return list with repositories being watched by the user.
                    If not give(which is by default), will return repositories being watched by the
                        authenticated user.
        :kwarg page: returns repositories from the given page. By default is set to 1.
        """
        url = f"{self._url}{f'/users/{username}' if username else '/user'}/subscriptions?page={page}"

        items = [
            model.create_class("Subscriber", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def subscribed(self, owner, repo):
        """
        Returns information about repository's subscription.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/subscription"
        item = model.create_class(
            "Subscription", request.get(url, headers=self._headers)
        )
        return item

    def subscribe(self, owner, repo, **kwargs):
        """
        Subscribes the authenticated user to a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg subscribed: determines if notifications should be received from this repository.
        :kwarg ignored: determines if all notifications should be blocked from this repository.
        """
        url = f"{self._url}/repos/{owner}/{repo}/subscription"
        item = model.create_class(
            "Response", request.put(url, headers=self._headers, params=kwargs)
        )
        return item

    def unsubscribe(self, owner, repo):
        """
        Unsubscribe from a repository.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/subscription"
        return model.create_class("Status", request.delete(url, headers=self._headers))
