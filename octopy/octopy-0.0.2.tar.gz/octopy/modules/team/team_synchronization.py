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

    def all(self, groups_for, **kwargs):
        """
        Returns all idP groups for specific type.

        :param groups_for: can be `organization`, or `team`
        :kwarg org:
        :kwarg team_id:
        """
        if groups_for.lower() == "organization":
            org = kwargs.get("org")
            del kwargs["org"]
            url = f"{self._url}/orgs/{org}/team-sync/groups"
        elif groups_for.lower() == "team":
            team_id = kwargs.get("team_id")
            del kwargs["team_id"]
            url = f"{self._url}/teams/{team_id}/team-sync/group-mappings"

        items = [
            model.create_class("Group", item)
            for item in request.get(url, headers=self._headers)["groups"]
        ]
        return items

    def update(self, team_id, **kwargs):
        """
        Creates, updates, or removes a connection between a team and an IdP group.

        :param team_id: team's id
        :kwarg groups: list with objects
            :kwarg group_id: [required] group's id
            :kwarg group_name: [required] name of the idP groups
            :kwarg group_description: [required] description of the 
                idP group
        """
        url = f"{self._url}/teams/{team_id}/team-sync/group-mappings"
        items = [
            model.create_class("idP", item)
            for item in request.patch(url, headers=self._headers, params=kwargs)[
                "groups"
            ]
        ]
        return items
