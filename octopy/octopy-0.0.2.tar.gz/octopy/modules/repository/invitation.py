from octopy import request, model


class Invitation:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/invitations/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Invitation
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def repository(self, owner, repo, page=1):
        """
        Returns all invitations for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page, invitations to be returned; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/invitations?page={page}"
        items = [
            model.create_class("Invitation", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def remove(self, owner, repo, invitation_id):
        """
        Deletes an invitation.

        :param owner: owner's name
        :param repo: repo's name
        :param invitation_id: invitation's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/invitations/{invitation_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def update(self, owner, repo, invitation_id, **kwargs):
        """
        Updates an invitation.

        :param owner: owner's name
        :param repo: repo's name
        :param invitation_id: invitation's id
        :kwarg permissions: The permissions that the associated 
            user will have on the repository. 
            Valid values are read, write, and admin.
        """
        url = f"{self._url}/repos/{owner}/{repo}/invitations/{invitation_id}"
        return model.create_class(
            "Invitation", request.patch(url, headers=self._headers, params=kwargs)
        )

    def mine(self, page=1):
        """
        Get users invitations.

        :kwarg page: from which page invitations to be returned; default: 1
        """
        url = f"{self._url}/user/repository_invitations?page={page}"
        items = [
            model.create_class("User", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def accept(self, invitation_id):
        """
        Accepts an invitation.

        :param invitation_id: invitation's id
        """
        url = f"{self._url}/user/repository_invitations/{invitation_id}"
        return model.create_class("Status", request.patch(url, headers=self._headers))

    def decline(self, invitation_id):
        """
        Decline an invitation.

        :param invitation_id: invitation's id
        """
        url = f"{self._url}/user/repository_invitations/{invitation_id}"

        return model.create_class("Status", request.delete(url, headers=self._headers))
