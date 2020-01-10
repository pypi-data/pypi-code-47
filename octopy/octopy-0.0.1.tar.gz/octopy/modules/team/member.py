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

        """
        url = f"{self._url}/teams/{team_id}/members?page={page}"
        items = [
            model.create_class("Member", item)
            for item in request.get(urll, headers=self._headers, params=kwargs)
        ]
        return items

    def member(self, team_id, username):
        """

        """
        url = f"{self._url}/teams/{team_id}/members/{username}"
        return request.get(url, headers=self._headers)

    def create(self, team_id, username):
        """

        """
        url = f"{self._url}/teams/{team_id}/members/{username}"
        return request.put(url, headers=self._headers)

    def remove(self, team_id, username, membership=False):
        """
        """
        if membership:
            url = f"{self._url}/teams/{team_id}/memberships/{username}"
            return request.delete(url, headers=self._headers)
        url = f"{self._url}/teams/{team_id}/members/{username}"
        return request.delete(url, headers=self._headers)

    def membership(self, team_id, username):
        """
        """
        url = f"{self._url}/teams/{team_id}/memberships/{username}"
        return model.create_class("Membership", request.get(url, headers=self._headers))

    def modify(self, team_id, username, **kwargs):
        """

        """
        url = f"{self._url}/teams/{team_id}/memberships/{username}"
        return model.create_class(
            "Membership", request.put(url, headers=self._headers, params=kwargs)
        )

    def pending_invitations(self, team_id, page=1):
        """
        """
        url = f"{self._url}/teams/{team_id}/invitations?page={page}"
        items = [
            model.create_class("Invitation", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items
