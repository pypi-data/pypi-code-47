from octopy import request, model


class Feed:

    """
    Official documentation in Github: https://developer.github.com/v3/activity/feeds/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/ActivityFeeds.md
    """

    def __init__(self, url, headers, **kwargs):
        self._url = url
        self._headers = headers

    def all(self):
        """
        Returns all feeds available to the authenticated user.
        """
        url = f"{self._url}/feeds"
        return model.create_class("Feed", request.get(url, headers=self._headers))
