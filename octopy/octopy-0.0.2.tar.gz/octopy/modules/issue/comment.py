from octopy import request, model


class Comment:

    """
    Official GITHUB documentation: https://developer.github.com/v3/issues/comments/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Issue-Comment.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, issue_number, page=1, reactions=False, **kwargs):
        """
        Returns all comments on an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_numner: issue's number
        :kwarg page: from which page results to be returned, default: 1
        :kwarg reactions: if set to true, the result will contain information
            about reactions
        :kwarg since: only comments updated at or after this time are returned. 
        This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/comments?page={page}"

        headers = self._headers
        if reactions:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        items = [
            model.create_class("IssueComment", item)
            for item in request.get(url, headers=headers, params=kwargs)
        ]
        return items

    def repository(self, owner, repo, reactions=False, page=1, **kwargs):
        """
        Returns all comments in a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: page's number, default: 1
        :kwarg reactions: if set to true, it will include reactions in the result
        :kwarg sort: can be `created` or `updated``
        :kwarg direction: `asc` or `desc`
        :kwarg since: only comments updated at or after this time are returned.
            This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/comments?page={page}"

        headers = self._headers
        if reactions:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        items = [
            model.create_class("RepoComment", item)
            for item in request.get(url, headers=headers, params=kwargs)
        ]
        return items

    def get(
        self, owner, repo, comment_id, reactions=False, performed_via_github_app=False,
    ):
        """
        Returns a single comment.

        :param owner: owner's name
        :param repo: repo's name
        :param comment_id: comment's id
        :kwarg reactions: if set to true, it will include reactions in the result
        :kwarg performed_via_github_app:
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}"

        headers = self._headers
        if performed_via_github_app:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.machine-man-preview"
        elif reactions:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        return model.create_class("Comment", request.get(url, headers=headers))

    def create(self, owner, repo, issue_number, **kwargs):
        """
        Creates a comment to an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg body: comment's body
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/comments"
        return model.create_class(
            "Comment", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, comment_id, **kwargs):
        """
        Updates a comment.

        :param owner: owner's name
        :param repo: repo's name
        :param comment_id: comment's id
        :kwarg body: comment's new body
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}"
        return model.create_class(
            "Comment", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, comment_id):
        """
        Deletes a comment.

        :param owner: owner's name
        :param repo: repo's name
        :param comment_id: comment's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}"
        return request.delete(url, headers=self._headers)
