from octopy import request, model


class Emoji:

    """
    Official GITHUB documentation: https://developer.github.com/v3/emojis/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Miscellaneous-Emoji.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self):
        """
        Returns all emojis.
        """
        url = f"{self._url}/emojis"
        return model.create_class("Emoji", request.get(url, headers=self._headers))
