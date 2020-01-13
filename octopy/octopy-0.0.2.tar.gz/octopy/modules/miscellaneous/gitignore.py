from octopy import request, model


class Gitignore:

    """
    Official GITHUB documentation: https://developer.github.com/v3/gitignore/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Miscellaneous-Gitignore.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self):
        """
        Returns all templates for a gitignore.
        """
        url = f"{self._url}/gitignore/templates"
        return request.get(url, headers=self._headers)

    def template(self, name):
        """
        Returns a single template for a gitignore.
        """
        url = f"{self._url}/gitignore/templates/{name}"
        return model.create_class("GitIgnore", request.get(url, headers=self._headers))
