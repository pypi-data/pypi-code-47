from octopy import request, model


class Blob:

    """
    Official GITHUB documentation: https://developer.github.com/v3/git/blobs/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/GitData-Blob.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def get(self, owner, repo, file_sha):
        """

        :param owner: owner.s name
        :param repo: repo's name
        :param file_sha: file sha
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/blobs/{file_sha}"
        return model.create_class("Blob", request.get(url, headers=self._headers))

    def create(self, owner, repo, **kwargs):
        """

        :param owner: owner's name
        :param repo: repo's name
        :kwarg content: [required] blob's content
        :kwarg encoding: encoding used for the content
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/blobs"
        return model.crate_class(
            "Blob", request.post(url, headers=self._headers, params=kwargs)
        )
