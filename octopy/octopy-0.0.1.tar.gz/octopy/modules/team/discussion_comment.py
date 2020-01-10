from octopy import model, request


class DiscussionComment:

    """
    Official GITHUB documentation: https://developer.github.com/v3/teams/discussion_comments/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/TeamDiscussionComment.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, team_id, discussion_number, page=1, **kwargs):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments?page={page}"
        items = [
            model.create_class("Comment", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def get(self, team_id, discussion_number, comment_number):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        return model.create_class("Comment", request.get(url, headers=self._headers))

    def create(self, team_id, discussion_number, **kwargs):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments"
        return model.create_class(
            "Comment", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, team_id, discussion_number, comment_number, **kwargs):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        return model.create_class(
            "Comment", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, team_id, discussion_number, comment_number):
        """

        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        return request.delete(url, headers=self._headers)
