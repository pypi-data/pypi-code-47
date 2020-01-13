from octopy import request, model

from .installation import Installation
from .oauth import OAuth


class App:

    """
    Official documentation in Github: https://developer.github.com/v3/apps/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/App.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.machine-man-preview+json"

        self.installations = Installation(url, headers)
        self.oauth_apis = OAuth(url, headers)

    def get(self, app_slug):
        """
        Returns a single app.

        :param app_slug: name of your app
        """
        url = f"{self._url}/apps/{app_slug}"
        return model.create_class("App", request.get(url, headers=self._headers))

    def app(self):
        """
        Returns an app associated with the authenticated credentials used.
        A JWT must be used for accessing this endpoint.
        """
        url = f"{self._url}/app"
        return model.create_class("App", request.get(url, headers=self._headers))

    def all(self, page=1):
        """
        Returns all installations.

        :kwarg page: from which page, results to be returned; default: 1
        """
        url = f"{self._url}/app/installations?page={page}"
        items = [
            model.create_class("Installation", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def installation(
        self, installation_id=None, org=None, owner=None, repo=None, username=None
    ):
        """
        Returns a single installation.

        :kwarg installation_id: installation's id
        :kwarg org: if given, it will return an org installation
        :kwarg owner: if given(with repo),it will return repository installation
        :kwarg repo: repo's name
        :kwarg username: user's name
        """
        if org:
            url = f"{self._url}/orgs/{org}/installation"
        elif owner and repo:
            url = f"{self._url}/repos/{owner}/{repo}/installation"
        elif installation_id:
            url = f"{self._url}/app/installations/{installation_id}"
        elif username:
            url = f"{self._url}/users/{username}/installation"
        else:
            raise TypeError("Invalid choice.")

        return model.create_class(
            "Installation", request.get(url, headers=self._headers)
        )

    def remove(self, installation_id):
        """
        Deletes an installation.

        :param installation_id: installation's id
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.gambit-preview+json"

        url = f"{self._url}/app/installations/{installation_id}"
        return model.create_class("Status", request.delete(url, headers=headers))

    def create_installation_token(self, installation_id, **kwargs):
        """
        Creates an installation access token.

        :param installation_id: installation's id
        :kwarg repository_ids: list with repository ids that the installation
            token can access
        :kwarg permissions: permissions granted to the access token.
        """
        url = f"{self._url}/installations/{installation_id}/access_tokens"
        return model.create_class(
            "InstallationToken", request.post(url, headers=self._headers, params=kwargs)
        )

    def create(self, code):
        """
        Creates an app from a manifest.

        :param code:
        """
        url = f"{self._url}/app-manifests/{code}/conversions"
        return model.create_class("App", request.post(url, headers=self._headers))
