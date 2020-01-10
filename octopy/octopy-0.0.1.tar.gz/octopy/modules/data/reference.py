from octopy import request, model


class Reference:

    """
    Official GITHUB documentation: https://developer.github.com/v3/git/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/GitData-Reference.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def get(self, owner, repo, ref):
        """
        Returns a single reference.

        :param owner: owner's name
        :param repo: repo's name
        :param ref: ref
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/ref/{ref}"
        return model.create_class("Reference", request.get(url, headers=self._headers))

    def matching(self, owner, repo, ref, page=1):
        """
        Returns all references, matching the supplied name.

        :param owner: owner's name
        :param repo: repo's name
        :param ref: ref
        :kwarg page: page from which results to be returned. default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/matching-refs/{ref}?page={page}"
        items = [
            model.create_class("MatchingReference", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def create(self, owner, repo, **kwargs):
        """
        Creates a reference.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg ref: [required] name of the fully qualified reference.
        :kwarg sha: [required] sha1 value of this rerefence.
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/refs"
        return model.create_class(
            "Reference", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, ref, **kwargs):
        """
        Updates a reference.

        :param owner: owner's name
        :param repo: repo's name
        :param ref: ref
        :kwarg sha: [required] sha1 value of this reference
        :kwarg force: if set to true, overwrite your work. Default: false
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/refs/{ref}"
        return model.create_class(
            "Reference", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, ref):
        """
        Deletes a reference.

        :param owner: owner's name
        :param repo: repo's name
        :param ref: ref
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/refs/{ref}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
