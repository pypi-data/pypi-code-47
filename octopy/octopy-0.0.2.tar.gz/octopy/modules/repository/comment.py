from octopy import request, model


class Comment:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/comments/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Comment
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1):
        """
        Returns all comments for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page comments to be returned; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/comments?page={page}"
        items = [
            model.create_class("RepositoryComment", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def commit(self, owner, repo, commit_sha, page=1):
        """
        Returns all comments for a given commit.

        :param owner: owner's name
        :param repo: repo's name
        :param commit_sha: commit's ha
        :kwarg page: from which page comments to be returned; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/commits/{commit_sha}/comments?page={page}"
        items = [
            model.create_class("CommitComment", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def create(self, owner, repo, commit_sha, **kwargs):
        """
        Creates a comment to a given commit.

        :param owner: owner's name
        :param repo: repo's name
        :param commit_sha: commit's sha
        :kwarg body: [required] content of the comment
        :kwarg path: relative path of the file to comment on
        :kwarg position: line index in the diff to comment on
        """
        url = f"{self._url}/repos/{owner}/{repo}/commits/{commit_sha}/comments"
        return model.create_class(
            "CommitComment", request.post(url, headers=self._headers, params=kwargs)
        )

    def get(self, owner, repo, comment_id, reactions=False):
        """
        Returns a single comment.

        :param owner: owner's name
        :param repo: repo's name 
        :param comment_id: comment's id
        """

        headers = self._headers
        if reactions:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        url = f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}"
        return model.create_class("CommitComment", headers=headers)

    def update(self, owner, repo, comment_id, **kwargs):
        """
        Updates a commit comment.

        :param owner: owner's name
        :param repo: repo's name
        :param comment_id: comment's id
        :kwarg body: [required] content of the comment
        """
        url = f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}"
        return model.create_class(
            "CommitComment", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, comment_id):
        """
        Deletes a comment.

        :param owner: owner's name
        :param repo: repo's name
        :param comment_id: comment's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
