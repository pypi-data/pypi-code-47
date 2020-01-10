from octopy import request, model


class Comment:

    """
    Official documentaion at GITHUB: https://developer.github.com/v3/gists/comments/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/GistComment.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, gist_id, page=1):
        """
        Returns all comments of a given gist.

        :param gist_id: gist's id
        :kwarg page: returns all comments from a given page, by default
            is set to 1.
        """
        url = f"{self._url}/gists/{gist_id}/comments?page={page}"
        items = [
            model.create_class("Comment", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, gist_id, comment_id):
        """
        Returns a single comment.

        :param gist_id: gist's id
        :param comment_id: coment's id
        """
        url = f"{self._url}/gists/{gist_id}/comments/{comment_id}"
        return model.create_class("Comment", request.get(url, headers=self._headers))

    def comment(self, gist_id, **kwargs):
        """
        Creates a coment in a given gist.

        :param gist_id: gist's id.
        :kwarg body: body of the comment
        """
        url = f"{self._url}/gists/{gist_id}/comments"
        return model.create_class(
            "Comment", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, gist_id, comment_id, **kwargs):
        """
        Updates a comment.

        :param gist_id: gist's id
        :param comment_id: comment's id
        :kwarg body: body of the comment
        """
        url = f"{self._url}/gists/{gist_id}/comments/{comment_id}"
        return model.create_class(
            "Comment", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, gist_id, comment_id):
        """
        Deletes a comment.

        :param gist_id: gist's id
        :param comment_id: comment's id
        """
        url = f"{self._url}/gists/{gist_id}/comments/{comment_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
