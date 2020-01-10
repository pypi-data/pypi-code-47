from octopy import request, model


class Commit:

    """
    Official GITHUB documentation: https://developer.github.com/v3/git/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/GitData-Commit.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def get(self, owner, repo, commit_sha):
        """
        Returns a single commit.

        :param owner: owner's name
        :param repo: repo's name
        :param commit_sha: commit's sha
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/commits/{commit_sha}"
        return model.create_class("Commit", request.get(url, headers=self._headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates a commit.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg message: [required] commit message
        :kwarg tree: [required] sha of the tree object
        :kwarg parents: [required] shas of the commits that are parents of this commit
        :kwarg author: 
            :kwarg name: author's name
            :kwarg email: author's email
            :kwarg date: indicates when the commit was authored
        :kwarg commiter:
            :kwarg name: author's name
            :kwarg email: author's email
            :kwarg date: indicates when the commit was authored
        :kwarg signature: PGP signature of the commit
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/commits"
        return model.create_class(
            "Commit", request.post(url, headers=self._headers, params=kwargs)
        )
