from octopy import request, model


class RateLimit:

    """
    Official GITHUB documentation: https://developer.github.com/v3/rate_limit/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Miscellaneous-RateLimit.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def get(self):
        """
        Returns user's rate limit status.
        """
        url = f"{self._url}/rate_limit"
        return model.create_class("RateLimit", request.get(url, headers=self._headers))
