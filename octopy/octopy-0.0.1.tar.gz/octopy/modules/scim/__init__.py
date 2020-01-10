from octopy import request, model


class Scim:

    """
    Official GITHUB documentation: https://developer.github.com/v3/projects/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Projects.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def users(self, org, **kwargs):
        """

        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users"
        return model.create_class(
            "User", request.get(url, headers=self._headers, params=kwargs)
        )

    def user(self, org, scim_user_id):
        """

        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users/{scim_user_id}"
        return model.create_class("User", request.get(url, headers=self._headers))

    def invite(self, org, **kwargs):
        """

        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users"
        return model.create_class(
            "User", request.post(url, headers=self._headers, params=kwargs)
        )

    def replace(self, org, scim_user_id, **kwargs):
        """

        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users/{scim_user_id}"
        return model.create_class(
            "User", request.put(url, headers=self._headers, params=kwargs)
        )

    def update(self, org, scim_user_id, **kwargs):
        """

        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users/{scim_user_id}"
        return model.create_class(
            "User", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, org, scim_user_id):
        """

        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users/{scim_user_id}"
        return request.delete(url, headers=self._headers)
