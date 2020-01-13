from octopy import model, request


class Discussion:

    """
    Official GITHUB documentation: https://developer.github.com/v3/teams/discussions/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/TeamDiscussion.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, team_id, page=1, reactions=False, **kwargs):
        """
        Returns all discussions for a team.

        :param team_id: team's id
        :kwarg page: from which page discussions to be returned
        :kwarg reactions: specifies, should the final result to include, or
            not a reactions summary
        :kwarg direction: specifies the order of the final result, can be
            `asc`, or `desc`; default: `desc`
        """
        headers = self._headers
        if reactions:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        url = f"{self._url}/teams/{team_id}/discussions?page={page}"
        items = [
            model.create_class("Discussion", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def get(self, team_id, discussion_number):
        """
        Returns a single discussion for a team.

        :param team_id: team's id
        :param disucssion_number: discussion's number
        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}"
        return model.create_class("Discussion", request.get(url, headers=self._headers))

    def create(self, team_id, **kwargs):
        """
        Creates a discussion for a team.

        :param team_id: team's id
        :kwarg title: [required] title of the discussion
        :kwarg body: [required] body of post's discussion
        :kwarg private: specifies the level of access for the discussion;
        """
        url = f"{self._url}/teams/{team_id}/discussions"
        return model.create_class(
            "Discussion", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, team_id, discussion_number, **kwargs):
        """
        Updates a discussion.

        :param team_id: team's id
        :param discussion_number: discussion's number
        :kwarg title: new title of the discussion
        :kwarg body: new post's body text
        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}"
        return model.create_class(
            "Discussion", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, team_id, discussion_number):
        """
        Deletes a discussion.

        :param team_id: team's id
        :param discussion_number: discussion's number
        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
