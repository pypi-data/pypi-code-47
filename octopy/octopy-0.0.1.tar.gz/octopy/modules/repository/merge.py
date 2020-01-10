from octopy import request, model


class Merge:

    """
    Official GITHUB documentation: 
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def merge(self, owner, repo, **kwargs):
        """
        Performs a merge.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg base: [required] name of the base branch
        :kwarg head: [required] head to merge
        :kwarg commit_message: message for the merge commit
        """
        url = f"{self._url}/repos/{owner}/{repo}/merges"
        return model.create_class(
            "Merge", request.post(url, headers=self._headers, params=kwargs)
        )
