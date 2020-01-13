from octopy import request, model


class Scim:

    """
    Official GITHUB documentation: https://developer.github.com/v3/scim/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Scim.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def users(self, org, **kwargs):
        """
        Returns a list of provisioned identities.

        :param org: org's name
        :kwarg startIndex: Used for pagination: the index of the first result to return.
        :kwarg count: Used for pagination: the number of results to return.
        :kwarg filter: Filters results 
            using the equals query 
            parameter operator (eq). 
            You can filter results that are equal 
            to id, userName, emails, and external_id. For example, to search for an identity with the userName Octocat, you would use this query: ?filter=userName%20eq%20\"Octocat\".
        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users"
        return model.create_class(
            "User", request.get(url, headers=self._headers, params=kwargs)
        )

    def user(self, org, scim_user_id):
        """
        Returns all details for a given user.

        :param org: org's name
        :param scim_user_id: scim user's id
        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users/{scim_user_id}"
        return model.create_class("User", request.get(url, headers=self._headers))

    def invite(self, org, **kwargs):
        """
        Invites a user.

        :param org: org's name
        :kwarg userName: user's name
        :kwarg name:
        :kwarg emails:
        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users"
        return model.create_class(
            "User", request.post(url, headers=self._headers, params=kwargs)
        )

    def replace(self, org, scim_user_id, **kwargs):
        """
        Replaces the information for a given user.

        :param org: org's name
        :param scim_user_id: scim user's id
        :kwarg userName:
        :kwarg name:
        :kwarg emails:
        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users/{scim_user_id}"
        return model.create_class(
            "User", request.put(url, headers=self._headers, params=kwargs)
        )

    def update(self, org, scim_user_id, **kwargs):
        """
        Updates a user atribute.

        :param org: org's name
        :param scim_user_id: scim user's id
        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users/{scim_user_id}"
        return model.create_class(
            "User", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, org, scim_user_id):
        """
        Removes a user from organization.

        :param org: org's name
        :param scim_user_id: scim user's id
        """
        url = f"{self._url}/scim/v2/organizations/{org}/Users/{scim_user_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
