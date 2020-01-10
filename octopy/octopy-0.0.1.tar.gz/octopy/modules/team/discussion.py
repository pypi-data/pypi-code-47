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

    def all(self, team_id, page=1, **kwargs):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions?page={page}"
        items = [
            model.create_class("Discussion", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def get(self, team_id, discussion_number):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}"
        return model.create_class("Discussion", request.get(url, headers=self._headers))

    def create(self, team_id, **kwargs):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions"
        return model.create_class(
            "Discussion", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, team_id, discussion_number, **kwargs):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}"
        return model.create_class(
            "Discussion", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, team_id, discussion_number):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}"
        return request.delete(url, headers=self._headers)
