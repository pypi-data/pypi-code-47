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

    def all(self, team_id, discussion_number, page=1, reactions=False, **kwargs):
        """
        Returns all comments for a discussion.

        :param team_id: team's id
        :param discussion_number: discussion's number
        :kwarg page: page from which comments to be returned
        :kwarg reactions: specifies should the final result include, or not
            reactions summary
        :kwarg direction: can be `asc`, or `desc`; default: `desc`
        """
        headers = self._headers
        if reactions:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments?page={page}"
        items = [
            model.create_class("Comment", item)
            for item in request.get(url, headers=headers, params=kwargs)
        ]
        return items

    def get(self, team_id, discussion_number, comment_number):
        """
        Returns a single comment.

        :param team_id: team's id
        :param discussion_numner: discussion's number
        :param comment_number: comment's number
        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        return model.create_class("Comment", request.get(url, headers=self._headers))

    def create(self, team_id, discussion_number, **kwargs):
        """
        Creates a comment to a given discussion.

        :param team_id: team's id
        :param discussion_number: discussion's numbr
        :kwarg body: body of the comment
        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments"
        return model.create_class(
            "Comment", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, team_id, discussion_number, comment_number, **kwargs):
        """
        Updates a comment.

        :param team_id: team's id
        :param discussion_number: discussion's number
        :param comment_number: comment's number
        :kwarg body: new body of the comment
        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        return model.create_class(
            "Comment", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, team_id, discussion_number, comment_number):
        """
        Deletes a comment from a discussion.

        :param team_id: team's id
        :param discussion_number: discussion's number
        :param comment_number: comment's number
        """
        url = f"{self._url}/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
