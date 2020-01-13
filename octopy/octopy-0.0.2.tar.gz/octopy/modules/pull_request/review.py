from octopy import request, model


class Review:

    """
    Official GITHUB documentation: https://developer.github.com/v3/pulls/reviews/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Reviews.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, pull_number, page=1):
        """
        Returns all reviews on a pull request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg page: from which page, reveiws to be returned; default: 1
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews?page={page}"
        )
        items = [
            model.create_class("Review", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, owner, repo, pull_number, review_id):
        """
        Returns a single review.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :param review_id: review's id
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        )
        return model.create_class("Review", request.get(url, headers=self._headers))

    def remove(self, owner, repo, pull_number, review_id):
        """
        Deletes a review.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :param review_id: review's id
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        )
        return model.create_class("Review", request.delete(url, headers=self._headers))

    def comments(self, owner, repo, pull_number, review_id, page=1):
        """
        Returns all comments on a review.

        :param owner: owner's name
        :param repo:  repo's name
        :param pull_number: pull reques'ts number
        :param review_id: review's id
        :kwarg page: from which page comments to be returned; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments?page={page}"
        items = [
            model.create_class("ReviewComment", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def create(self, owner, repo, pull_number, **kwargs):
        """
        Creates a review.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull's number
        :kwarg commit_id:  The SHA of the commit that needs a review
        :kwarg body: [required] body text of the pull request review
        :kwarg event: review action you want to perform. 
            Can be `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`
        :kwarg comments: list with draft review comment objects
            :kwarg path: [required] relative path to the file that necessitates a review
                comment
            :kwarg position: [required] position in the diff where you want
                to add a review comment
            :kwarg body: [required] text of the review comment
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews"
        return model.create_class(
            "Review", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, pull_number, review_id, **kwargs):
        """
        Updates a review.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :param review_id: review's id
        :kwarg body: [required] body text of the pull request review
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        )
        return model.create_class(
            "Review", request.put(url, headers=self._headers, params=kwargs)
        )

    def submit(self, owner, repo, pull_number, review_id, **kwargs):
        """
        Submits a pull request review.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :param review_id: review's id
        :kwarg body: body text of the review
        :kwarg event: [required] can be `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`.
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events"
        return model.create_class(
            "Review", request.post(url, headers=self._headers, params=kwargs)
        )

    def dismiss(self, owner, repo, pull_number, review_id, **kwargs):
        """
        Deletes a pull request review.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :param review_id: review's id
        :kwarg message: reason for the dismissal
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals"
        return model.create_class(
            "Review", request.put(url, headers=self._headers, params=kwargs)
        )
