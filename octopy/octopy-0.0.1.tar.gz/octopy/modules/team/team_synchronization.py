from octopy import model, request


class TeamSynchronization:

    """
    Official GITHUB documentation: https://developer.github.com/v3/teams/team_sync/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/TeamSynchronization.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def organizations(self, org):
        """
        """
        url = f"{self._url}/orgs/{org}/team-sync/groups"
        return model.create_class("Org", request.get(url, headers=self._headers))

    def idP(self, team_id):
        """

        """
        url = f"{self._url}/teams/{team_id}/team-sync/group-mappings"
        return model.create_class("idP", request.get(url, headers=self._headers))

    def update(self, team_id, **kwargs):
        """

        """
        url = f"{self._url}/teams/{team_id}/team-sync/group-mappings"
        return model.create_class(
            "idP", request.patch(url, headers=self._headers, params=kwargs)
        )
