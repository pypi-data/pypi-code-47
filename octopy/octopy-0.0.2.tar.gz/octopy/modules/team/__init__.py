from octopy import model, request

from .discussion import Discussion
from .discussion_comment import DiscussionComment
from .member import Member
from .team_synchronization import TeamSynchronization


class Team:

    """
    Official GITHUB documentation: https://developer.github.com/v3/teams
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Teams.md
    """

    def __init__(self, url, headers):
        self.discussions = Discussion(url, headers)
        self.discussion_comments = DiscussionComment(url, headers)
        self.members = Member(url, headers)
        self.team_synchronizations = TeamSynchronization(url, headers)

        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.inertia-preview+json"

    def all(self, org, page=1):
        """
        Returns all teams for an org.

        :param org: org's name
        :kwarg page: from which page, teams to be returned; default: 1
        """
        url = f"{self._url}/orgs/{org}/teams?page={page}"
        items = [
            model.create_class("Team", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, by, **kwargs):
        """
        Returns a single team.

        :param by: specifies the type of parameters, which will be used
            to determine the team to be returned; can be `id`, or `name`
        :kwarg team_id: if by is set to id, team_id must be given
        :kwarg org: if by is set to name, org and team_slug must be given
        :kwarg team_slug:
        """
        if by == "id":
            team_id = kwargs.get("team_id")
            url = f"{self._url}/teams/{team_id}"
        elif by == "name":
            org = kwargs.get("org")
            team_slug = kwargs.get("team_slug")
            url = f"{self._url}/orgs/{org}/teams/{team_slug}"
        else:
            raise TypeError("Invalid choice.")

        return model.create_class("Team", request.get(url, headers=self._headers))

    def create(self, org, **kwargs):
        """
        Adds a team to an org.

        :param org: org's name
        :kwarg name: [required] name of the team
        :kwarg description: short description of the team
        :kwarg maintainers: list with ids of organization members
        :kwarg repo_names: list with full name of repositories, to add
            to the team
        :kwarg privacy: The level of privacy this team should have. The options are:
            For a non-nested team:
            * secret - only visible to organization owners and members of this team.
            * closed - visible to all members of this organization.
            Default: secret
            For a parent or child team:
            * closed - visible to all members of this organization.
            Default for child team: closed
        :kwarg parent_team_id:      The ID of a team to set as the parent team.
        """
        url = f"{self._url}/orgs/{org}/teams"
        return model.create_class(
            "Team", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, team_id, by=None, **kwargs):
        """
        Updates a team or team repository.

        :param team_id: team's id
        :kwarg by: sets the action to be taken;
            can be `owner`, `project`, or `none`;
            default: none, which updates only the team

        If `by` == None
            :kwarg name:
            :kwarg description:
            :kwarg privacy:
            :kwarg parent_team_id
    
        If `by` == `owner`
            :kwarg permission:

        If `by` == `project`
            :kwarg permission:
        """
        if by == "owner":
            owner = kwargs.get("owner")
            repo = kwargs.get("repo")
            del kwargs["owner"]
            del kwargs["repo"]

            url = f"{self._url}/teams/{team_id}/repos/{owner}/{repo}"
            return model.create_class(
                "Team", request.put(url, headers=self._headers, params=kwargs)
            )
        elif by == "project":
            project_id = kwargs.get("project_id")
            del kwargs["project_id"]
            url = f"{self._url}/teams/{team_id}/projects/{project_id}"
            return model.create_class(
                "Team", request.put(url, headers=self._headers, params=kwargs)
            )

        url = f"{self._url}/teams/{team_id}"
        return model.create_class(
            "Team", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, team_id, by=None, page=1):
        """

        """
        if by == "repository":
            owner = kwargs.get("owner")
            repo = kwargs.get("repo")

            del kwargs["owner"]
            del kwargs["repo"]

            url = f"{self._url}/teams/{team_id}/repos/{owner}/{repo}"
        elif by == "project":
            project_id = kwargs.get("project_id")
            del kwargs["project_id"]
            url = f"{self._url}/teams/:team_id/projects/{project_id}"
        else:
            url = f"{self._url}/teams/{team_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def children(self, team_id, page=1):
        """
        Returns child teams for a given team.

        :param team_id: team's id
        :kwarg page: from which page, teams to be returned; default: 1
        """
        url = f"{self._url}/teams/{team_id}/teams?page={page}"
        items = [
            model.create_class("Team", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def repositories(self, team_id, page=1):
        """
        Returns all repositories for a team.

        :param team_id: team's id
        :kwarg page: from which page repositories to be returned; default: 1
        """
        url = f"{self._url}/teams/{team_id}/repos?page={page}"
        items = [
            model.create_class("Repository", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def manage_repository_check(self, team_id, owner, repo, with_permissions=False):
        """
        Checks if a team manages a repository.

        :param team_id: team's id
        :param owner: owner's name
        :param repo: repo's name
        :kwarg with_permissions: if set to true, will include information
            about the permission level of the team to the given repository
        """
        headers = self._headers
        if with_permissions:
            headers["Accept"] = "application/vnd.github.v3.repository+json"

        url = f"{self._url}/teams/{team_id}/repos/{owner}/{repo}"
        return model.create_class("Status", request.get(url, headers=headers))

    def user(self, page=1):
        """
        Returns all teams of the authenticated user.

        :kwarg page: from which page, teams to be returned; default: 1
        """
        url = f"{self._url}/user/teams?page={page}"
        items = [
            model.create_class("Team", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def projects(self, team_id, page=1):
        """
        Returns all projects managed by a team.

        :param team_id: team's id
        :kwarg page: from which page projects to be returned; default: 1
        """
        url = f"{self._url}/teams/{team_id}/projects?page={page}"
        items = [
            model.create_class("Project", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def review(self, team_id, project_id):
        """
        Checks the permissions for a team for a given project.

        :param team_id: team's id
        :param project_id:  project's id
        """
        url = f"{self._url}/teams/{team_id}/projects/{project_id}"
        return request.get(url, headers=self._headers)
