from octopy import request, model


class Commit:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/commits/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Commit
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1, **kwargs):
        """
        Returns all commits for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page commits to be returned
        :kwarg sha: SHA or branch to start listing commits from
        :kwarg path: only commits containing this file path will be returned
        :kwarg author: it will filter results by given commit author
        :kwarg since: it will filter results by given date
        :kwarg until: it will filter results before given date
        """
        url = f"{self._url}/repos/{owner}/{repo}/commits?page={page}"
        items = [
            model.create_class("Commit", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def get(self, owner, repo, ref):
        """
        Returns a single commit.

        :param owner: owner's name
        :param repo: repo's name
        :param ref: commit's ref
        """
        url = f"{self._url}/repos/{owner}/{repo}/commits/{ref}"
        return model.create_class("Commit", request.get(url, headers=self._headers))

    def compare(self, owner, repo, base, head):
        """
        Compares two commits.

        :param owner: owner's name
        :param repo: repo's name
        :param base:
        :param head:
        """
        url = f"{self._url}/repos/{owner}/{repo}/compare/{base}...{head}"
        return model.create_class("Comparison", request.get(url, head=self._headers))

    def branches(self, owner, repo, commit_sha):
        """
        Returns all branches for a commit.

        :param owner: owner's name
        :param repo: repo's name
        :param commit_sha: commit's sha
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.groot-preview+json"

        url = (
            f"{self._url}/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head"
        )
        items = [
            model.create_class("Branch", item)
            for item in request.get(url, head=self._headers)
        ]
        return items

    def pull_requests(self, owner, repo, commit_sha, page=1):
        """
        Returns all pull requests for a commit.

        :param owner: owner's name
        :param repo: repo's name
        :param commit_sha: commit's sha
        :kwarg page: from which page pull requests to be returned; default: 1
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.groot-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/commits/{commit_sha}/pulls?page={page}"
        items = [
            model.create_class("PullRequestCommit", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items
