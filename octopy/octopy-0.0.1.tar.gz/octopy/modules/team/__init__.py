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

        """
        url = f"{self._url}/orgs/{org}/teams?page={page}"
        items = [
            model.create_class("Team", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, by, **kwargs):
        """

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

        """
        url = f"{self._url}/orgs/{org}/teams"
        return model.create_class(
            "Team", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, by, team_id, **kwargs):
        """

        """
        if by == "owner":
            pass
        elif by == "project":
            pass
        else:
            url = f"{self._url}/teams/{team_id}"
        return model.create_class(
            "Team", request.patch(url, headers=self._headers, params=kwargs)
        )

    def children(self, team_id, page=1):
        """

        """
        url = f"{self._url}/teams/{team_id}/teams?page={page}"
        items = [
            model.create_class("Team", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def repositories(self, team_id, page=1):
        """

        """
        url = f"{self._url}/teams/{team_id}/repos?page={page}"
        items = [
            model.create_class("Team", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def manage_repository_check(self, team_id, owner, repo):
        """

        """
        url = f"{self._url}/teams/{team_id}/repos/{owner}/{repo}"
        # with info application/vnd.github.v3.repository+json
        return request.get(url, headers=self._headers)

    def remove(self, by, team_id, **kwargs):
        if by == "owner":
            url = f"{self._url}/teams/{team_id}/repos/{owner}/{repo}"
        elif by == "project":
            pass
        else:
            url = f"{self._url}/teams/{team_id}"

        return request.delete(url, headers=self._headers)

    def user(self, page=1):
        """
        """
        url = f"{self._url}/user/teams?page={page}"
        items = [
            model.create_class("UserTeam", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def projects(self, team_id, page=1):
        """

        """
        url = f"{self._url}/teams/{team_id}/projects?page={page}"
        items = [
            model.create_class("Project", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def review(self, team_id, project_id):
        url = f"{self._url}/teams/{team_id}/projects/{project_id}"
        return request.get(url, headers=self._headers)
