from .card import Card
from .collaborator import Collaborator
from .column import Column

from octopy import request, model


class Project:

    """
    Official GITHUB documentation: https://developer.github.com/v3/projects/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Projects.md
    """

    def __init__(self, url, headers):

        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.inertia-preview+json"

        self.cards = Card(url, self._headers)
        self.collaborators = Collaborator(url, self._headers)
        self.columns = Column(url, self._headers)

    def all(self, owner, repo, page=1, **kwargs):
        """
        Returns all projects in a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page projects to be returned, default: 1
        :kwarg state: indicates the state of the projects to return.
            Can be `open`(default), `closed`, or `all`
        """
        url = f"{self._url}/repos/{owner}/{repo}/projects?page={page}"
        items = [
            model.create_class("Project", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def organization(self, org, page=1, **kwargs):
        """
        Returns all projects of an organization.

        :param org: org's name
        :kwarg page: from which page projects to be returned
        :kwarg state: indicates the state of the projects to return.
            Can be `open`(default), `closed`, or `all`
        """
        url = f"{self._url}/orgs/{org}/projects?page={page}"
        items = [
            model.create_class("OrgProject", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def user(self, username, page=1, **kwargs):
        """
        Returns all projects of an user.

        :param username: user's name
        :kwarg page: from which page, projects to be returned. default: 1
        :kwarg state: indicates the state of the projects to return.
            Can be `open`(default), `closed`, or `all`
        """
        url = f"{self._url}/users/{username}/projects?page={page}"
        items = [
            model.create_class("UserProject", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def get(self, project_id):
        """
        Returns a single project.

        :param project_id: project's id
        """
        url = f"{self._url}/projects/{project_id}"
        return model.create_class("Project", request.get(url, headers=self._headers))

    def create(self, owner, repo, project_type="repository", **kwargs):
        """
        Creates a project.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg project_type: 
            Can be `repository`(default), `organization`, or `user`
        :kwarg name: [required] project's name
        :kwarg body: project's description
        """
        if project_type.lower() == "repository":
            url = f"{self._url}/repos/{owner}/{repo}/projects"
        elif project_type.lower() == "organization":
            url = f"{self._url}/orgs/{org}/projects"
        elif project_type.lower() == "user":
            url = f"{self._url}/user/projects"
        else:
            raise TypeError(f"Invalid project type: {project_type}.")

        return model.create_class(
            "Project", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, project_id, **kwargs):
        """
        Updates a project.

        :param project_id: project's id
        :kwarg name: [required] project's name
        :kwarg body: project's body
        """
        url = f"{self._url}/projects/{project_id}"
        return model.create_class(
            "Project", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, project_id):
        """
        Deletes a project.

        :param project_id: project's id
        """
        url = f"{self._url}/projects/{project_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
