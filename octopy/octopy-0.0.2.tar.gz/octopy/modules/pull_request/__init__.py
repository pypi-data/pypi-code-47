from .review import Review
from .review_comment import ReviewComment
from .review_request import ReviewRequest

from octopy import request, model


class PullRequest:

    """
    Official GITHUB documentation: https://developer.github.com/v3/pulls/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/PullRequests.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

        self.reviews = Review(url, headers)
        self.review_comments = ReviewComment(url, headers)
        self.review_requests = ReviewRequest(url, headers)

    def all(self, owner, repo, page=1, draft=False, locked=False):
        """
        Returns all pull requests of a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page, pull requests to be returned; default: 1
        :kwarg draft: if set to true, it will return information wheter the pull
            reuqest is in draft state.
        :kwarg locked: if set to true, it will return information whether the pull request
            is locked, or not.
        """
        headers = self._headers
        if draft or locked:
            headers = headers.copy()

        if draft:
            headers["Accept"] = "application/vnd.github.shadow-cat-preview+json"
        elif locked:
            headers["Accept"] = "application/vnd.github.sailor-v-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/pulls?page={page}"
        items = [
            model.create_class("PullRequest", item)
            for item in request.get(url, headers=headers)
        ]
        return items

    def get(self, owner, repo, pull_number, draft=False, locked=False):
        """
        Returns a single pull request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg draft: if set to true, it will return information wheter the pull
            reuqest is in draft state.
        :kwarg locked: if set to true, it will return information whether the pull request
            is locked, or not.
        """
        headers = self._headers
        if draft or locked:
            headers = headers.copy()

        if draft:
            headers["Accept"] = "application/vnd.github.shadow-cat-preview+json"
        elif locked:
            headers["Accept"] = "application/vnd.github.sailor-v-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}"
        return model.create_class("PullRequest", request.get(url, headers=headers))

    def create(self, owner, repo, draft=False, locked=False, **kwargs):
        """
        Creates a pull request.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg draft: if set to true, it will return information wheter the pull
            reuqest is in draft state.
        :kwarg locked: if set to true, it will return information whether the pull request
            is locked, or not.
        :kwarg title: [required] title of the new pull request
        :kwarg head: [required] name of the branch where your changes are implemented
        :kwarg base: [required] name of the branch you wan the changes pulled into
        :kwarg body:
        :kwarg mainainer_can_modify: indicates whether maintainers can modify
            the pull request
        :kwarg draft: indicates whether the pull request is draft
        """
        headers = self._headers
        if draft or locked:
            headers = headers.copy()

        if draft:
            headers["Accept"] = "application/vnd.github.shadow-cat-preview+json"
        elif locked:
            headers["Accept"] = "application/vnd.github.sailor-v-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/pulls"
        return model.create_class(
            "PullRequest", request.post(url, headers=headers, params=kwargs)
        )

    def update_branch(self, owner, repo, pull_number, draft=False, **kwargs):
        """
        Updates a pull request branch.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg draft:
        :kwarg expected_head_sha: the expected SHA of the pull request's HEAD ref. 
        """
        headers = self._headers
        if draft:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.shadow-cat-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/update-branch"
        return model.create_class(
            "PullRequest", request.put(url, headers=headers, param=kwargs)
        )

    def update(self, owner, repo, pull_number, draft=False, locked=False, **kwargs):
        """
        Updates a pull request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg draft:
        :kwarg locked:
          :kwarg title: title of the new pull request
        :kwarg head: name of the branch where your changes are implemented
        :kwarg base: name of the branch you wan the changes pulled into
        :kwarg body:
        :kwarg mainainer_can_modify: indicates whether maintainers can modify
            the pull request
        """
        headers = self._headers
        if draft or locked:
            headers = headers.copy()

        if draft:
            headers["Accept"] = "application/vnd.github.shadow-cat-preview+json"
        elif locked:
            headers["Accept"] = "application/vnd.github.sailor-v-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}"
        return model.create_class(
            "PullRequest", request.patch(url, headers=self._headers, params=kwargs)
        )

    def commits(self, owner, repo, pull_number, page=1):
        """
        Returns all commits on a pull request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg page: from which page commits to be returned; default: 1
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/commits?page={page}"
        )
        items = [
            model.create_class("Commit", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def files(self, owner, repo, pull_number, page=1):
        """
        Returns all files on a pull request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg page: from which page files to be returned; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/files?page={page}"
        items = [
            model.create_class("File", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def merged(self, owner, repo, pull_number):
        """
        Checks if a pull request has been merged.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/merge"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def merge(self, owner, repo, pull_number, **kwargs):
        """
        Merge's a pull request.

        :param owner: owner's name
        :param repo: repo's name
        :param pull_number: pull request's number
        :kwarg commit_title: title for the automatic commit message
        :kwarg commit_message: some extra details for the commit message
        :kwarg sha: SHA that pull request head must match to allow merge.
        :kwarg merged_method: Merge method to use. 
            Possible values are merge, squash or rebase. Default is merge.
        """
        url = f"{self._url}/repos/{owner}/{repo}/pulls/{pull_number}/merge"
        return model.create_class(
            "Merge", request.put(url, headers=self._headers, params=kwargs)
        )
