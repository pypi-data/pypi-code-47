from octopy import request, model


class Tag:

    """
    Official GITHUB documentation: https://developer.github.com/v3/git/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/GitData-Tag.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def get(self, owner, repo, tag_sha):
        """
        Returns a single tag.

        :param owner: owner's name
        :param repo: repo's name
        :param tag_sha: tag's sha
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/tags/{tag_sha}"
        return model.create_class("Tag", request.get(url, headers=self._headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates a tag.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg tag: [required] tag's name
        :kwarg message: [required] tag's message
        :kwarg object: [required] sha of the git object
        :kwarg type: [required] type of the object, which is tagged
        :kwarg tagger: 
            :kwarg name: author's name
            :kwarg email: author's email
            :kwarg date: when the object was tagged
        """
        url = f"{self._url}/repos/{owner}/{repo}/git/tags"
        return model.create_class(
            "Tag", request.post(url, headers=self._headers, params=kwargs)
        )
