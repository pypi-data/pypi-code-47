from octopy import model, request


class Member:

    """
    Official GITHUB documentation: https://developer.github.com/v3/teams/members/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/TeamMember.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, team_id, page=1, **kwargs):
        """
        Returns all members for a team.

        :param team_id: team's id
        :kwarg page: from which page, members to be returned
        :kwarg role: Filters members returned by their role in the team. Can be one of:
            * member - normal members of the team.
            * maintainer - team maintainers.
            * all - all members of the team.
        Default: all
        """
        url = f"{self._url}/teams/{team_id}/members?page={page}"
        items = [
            model.create_class("Member", item)
            for item in request.get(urll, headers=self._headers, params=kwargs)
        ]
        return items

    def create(self, team_id, username):
        """
        Adds a user to a team.

        :param team_id: team's id
        :param username: user's name
        """
        url = f"{self._url}/teams/{team_id}/members/{username}"
        return model.create_class("Status", request.put(url, headers=self._headers))

    def remove(self, team_id, username):
        """
        Removes a user from a team.

        :param team_id: team's id
        :param username: user's name
        """
        url = f"{self._url}/teams/{team_id}/memberships/{username}"
        return request.delete(url, headers=self._headers)

    def membership(self, team_id, username):
        """
        Check if a user has a membership with a team.

        :param team_id: team's id
        :param username: user's name
        """
        url = f"{self._url}/teams/{team_id}/memberships/{username}"
        return model.create_class("Membership", request.get(url, headers=self._headers))

    def modify(self, team_id, username, **kwargs):
        """
        Adds/Updates a membership of a user to a team.

        :param team_id: team's id
        :param username: user's name
        :kwarg role: specifies role of the user to the team
            Can be `member`(default), or `maintainer`
        """
        url = f"{self._url}/teams/{team_id}/memberships/{username}"
        return model.create_class(
            "Membership", request.put(url, headers=self._headers, params=kwargs)
        )

    def pending_invitations(self, team_id, page=1):
        """
        Returns all pending invitations for a team.

        :param team_id: team's id
        :kwarg page: from which page, invitations to be returned; default: 1
        """
        url = f"{self._url}/teams/{team_id}/invitations?page={page}"
        items = [
            model.create_class("Invitation", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items
