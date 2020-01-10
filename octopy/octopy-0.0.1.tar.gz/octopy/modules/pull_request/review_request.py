from octopy import request, model


class ReviewRequest:

    """
    Official GITHUB documentation: https://developer.github.com/v3/pulls/review_requests/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/ReviewRequest.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, pull_number, page=1):
        """
        Returns all review requests on a pull request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg page: from which page requests to be returned
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers?page={page}"
        items = [
            model.create_class("ReviewRequest", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def create(self, owner, repo, pull_number, **kwargs):
        """
        Creates a review request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg reviewers: list with user logins
        :kwarg team_reviewers: list with team sluggs
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"
        )
        return model.create_class(
            "ReviewRequest", request.post(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, pull_number, **kwargs):
        """
        Deletes a review request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg reviewers: list with user logins
        :kwarg team_reviewers: list with team slugs
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"
        )
        return model.create_class(
            "Status", request.delete(url, headers=self._headers, params=kwargs)
        )
