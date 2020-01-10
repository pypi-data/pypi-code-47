from octopy import request, model


class ReviewComment:

    """
    Official GITHUB documentation: https://developer.github.com/v3/pulls/comments/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/ReveiwComment.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(
        self,
        owner,
        repo,
        pull_number,
        multiline=False,
        reactions=False,
        page=1,
        **kwargs,
    ):
        """
        Returns all pull requests on a pull request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg multiline: if set to true, the result will include multi-line comments summary
        :kwarg reactions: if set to true, the result will include reactions summary
        :kwarg page: from which page comments to be returned; default: 1
        :kwarg sort: can be `created`, or `updated`
        :kwarg direction: can be `asc`, or `desc`
        :kwarg since: from when comments to be returned
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/comments?page={page}"
        )
        headers = self._headers
        if multiline or reactions:
            headers = headers.copy()

        if multiline:
            headers["Accept"] = "application/vnd.github.comfort-fade-preview+json"
        elif reactions:
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        items = [
            model.create_class("Comment", item)
            for item in request.get(url, headers=headers, params=kwargs)
        ]
        return items

    def get(
        self, owner, repo, pull_number, comment_id, multiline=False, reactions=False
    ):
        """
        Returns all comments in a repository.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :param comment_id: comment's id
        :kwarg multiline: if set to true, it will include multi-line comments summary
        :kwarg reactions: if set to true, it will include reactions summary
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}"
        headers = self._headers
        if multiline or repository:
            headers = headers.copy()

        if multiline:
            headers["Accept"] = "application/vnd.github.comfort-fade-preview+json"
        elif reactions:
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        return model.create_class("Comment", request.get(url, headers=headers))

    def create(self, owner, repo, pull_number, multiline=False, **kwargs):
        """
        Creates a comment review.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg multiline: if set to true, it will include a multiline comment summary
        :kwarg body: [required] text of the review comment
        :kwarg commit_id: [required] sha of the commit needing a comment
        :kwarg path: [required] relative path to the file
        :kwarg position: [required] position in the diff, where
            to add the comment
        :kwarg side: [required] Can be `left`, or `right`. Represents the side of
            the diff, that the pull request's changes appear on.
        :kwarg line: [required] line of the blob in the pull request diff that the
            comment applies to
        :kwarg start_line: [required] the first line in the pull request diff that
            your multi-line comment applies to.
        :kwarg start_side: [required] Can be `left`, or `right`
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/comments"
        headers = self._headers

        if multiline:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.comfort-fade-preview+json"

        return model.create_class(
            "Comment", request.post(url, headers=headers, params=kwargs)
        )

    def reply(self, owner, repo, pull_number, comment_id, multiline=False, **kwargs):
        """
        Creates a review comment reply.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :param comment_id: comment's id
        :kwarg multiline:
        :kwarg body: [required] text of the comment
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies"
        headers = self._headers
        if multiline:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.comfort-fade-preview+json"

        return model.create_class(
            "Reply", request.post(url, headers=headers, params=kwargs)
        )

    def update(self, owner, repo, comment_id, multiline=False, **kwargs):
        """
        Updates a comment.

        :param owner: owner's name
        :param repo: repo's name
        :param comment_id: comment's id
        :kwarg multiline: 
        :kwarg body:[required] text of the reply to the review comment
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}"
        headers = self._headers
        if multiline:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.comfort-fade-preview+json"

        return model.create_class(
            "Comment", request.patch(url, headers=headers, params=kwargs)
        )

    def remove(self, owner, repo, comment_id):
        """
        Deletes a comment.

        :param owner: owner's name
        :param repo: repo's name
        :param comment_id: comment's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
