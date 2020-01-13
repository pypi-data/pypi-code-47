from octopy import request, model


class Collaborator:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/collaborators/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Collaborator
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1, **kwargs):
        """
        Returns all collaborators for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page collaborators to be returned; default: 1
        :kwarg affiliation: Filter collaborators returned by their affiliation. 
            Can be one of:
            * outside: All outside collaborators of an organization-owned repository.
            * direct: All collaborators with permissions to an organization-owned repository, regardless of organization membership status.
            * all: All collaborators the authenticated user can see.
            Default: all
        """
        url = f"{self._url}/repos/{owner}/{repo}/collaborators?page={page}"
        items = [
            model.create_class("Collaborator", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def check(self, owner, repo, username):
        """
        Checks if a user is a collaborator.

        :param owner: owner's name
        :param repo: repo's name
        :param username: user's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/collaborators/{username}"
        return model.create_class("Status", request.get(url, headers=self.headers))

    def permission_level(self, owner, repo, username):
        """
        Returns the permission level of a user.

        :param owner: owner's name
        :param repo: repo's name
        :param username: user's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/collaborators/{username}/permission"
        return model.create_class(
            "PermissionLevel", request.get(url, headers=self._headers)
        )

    def create(self, owner, repo, username, **kwargs):
        """
        Adds a user as collaborator.

        :param owner: owner's name
        :param repo: repos' name
        :param username: user's name
        :kwarg permission: The permission to grant the collaborator. 
            Only valid on organization-owned repositories. Can be one of:
                * pull - can pull, but not push to or administer this repository.
                * push - can pull and push, but not administer this repository.
                * admin - can pull, push and administer this repository.
            Default: push
        """
        url = f"{self._url}/repos/{owner}/{repo}/collaborators/{username}"
        return model.create_class(
            "PermissionLevel", request.put(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, username):
        """
        Removes a user as collaborator.

        :param owner: owner's name
        :param repo: repo's name
        :param username: user's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/collaborators/{username}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
