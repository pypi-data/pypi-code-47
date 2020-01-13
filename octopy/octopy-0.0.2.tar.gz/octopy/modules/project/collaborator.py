from octopy import request, model


class Collaborator:

    """
    Official GITHUB documentation: https://developer.github.com/v3/projects/collaborators/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Project-Collaborators.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.inertia-preview+json"

    def all(self, project_id, page=1, **kwargs):
        """
        Returns all collaborators for a project.

        :param project_id: project's id
        :kwarg page: from which page collaborators to be returned
        :kwarg affiliation:
            Filters the collaborators by their affiliation. Can be one of:
                * outside: Outside collaborators of a 
                project that are not a member of the 
                project's organization.
                * direct: Collaborators with permissions 
                to a project, regardless of organization membership status.
                * all: All collaborators the authenticated user can see.
            Default: all
        """
        url = f"{self._url}/projects/{project_id}/collaborators?page={page}"
        items = [
            model.create_class("Collaborator", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def permission(self, project_id, username):
        """
        Returns collcatorator's permission level.

        :param project_id: project's id
        :param username: user's name
        """
        url = f"{self._url}/projects/{project_id}/collaborators/{username}/permission"
        return model.create_class(
            "UserPermission", request.get(url, headers=self._headers)
        )

    def create(self, project_id, username, **kwargs):
        """
        Adds a user as collaborator.

        :param project_id: project's id
        :param username: user's name
        :kwarg permission:
        The permission to grant the collaborator. 
        Note that, if you choose not to pass any parameters, 
        you'll need to set Content-Length to zero when 
        calling out to this endpoint. For more information, 
        see "HTTP verbs." Can be one of:
            * read - can read, but not write to or administer this project.
            * write - can read and write, but not administer this project.
            * admin - can read, write and administer this project.
        Default: write
        """
        url = f"{self._url}/projects/{project_id}/collaborators/{username}"
        return model.create_class(
            "Status", request.put(url, headers=self._headers, params=kwargs)
        )

    def remove(self, project_id, username):
        """
        Removes a user as collaborator.

        :param project_id: project's id
        :param username: user's name
        """
        url = f"{self._url}/projects/{project_id}/collaborators/{username}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
