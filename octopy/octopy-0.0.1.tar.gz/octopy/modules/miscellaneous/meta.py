from octopy import request, model


class Meta:

    """
    Official GITHUB documentation: https://developer.github.com/v3/meta/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Miscellaneous-Meta.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def get(self):
        """
        Returns all GITHUB IP addresses.
        """
        url = f"{self._url}/meta"
        return model.create_class("Meta", request.get(url, headers=self._headers))
