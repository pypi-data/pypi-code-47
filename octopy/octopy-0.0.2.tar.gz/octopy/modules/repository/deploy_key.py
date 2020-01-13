from octopy import request, model


class DeployKey:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/keys/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-DeployKey
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1):
        """
        Returns all deploy keys for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page, results to be returned; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/keys?page={page}"
        items = [
            model.create_class("DeployKey", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, owner, repo, key_id):
        """
        Returns a single deploy key.

        :param owner: owner's name
        :param repo: repo's name
        :param key_id: key's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/keys/{key_id}"
        return model.create_class("DeployKey", request.get(url, headers=self._headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates a deploy key.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg title: name for the key
        :kwarg key: [required] content of the key
        :kwarg read_only: If true, the key will only be 
            able to read repository contents. Otherwise, the 
            key will be able to read and write.
        """
        url = f"{self._url}/repos/{owner}/{repo}/keys"
        return model.create_class(
            "DeployKey", request.post(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, key_id):
        """
        Deletes a key.

        :param owner: owner's name
        :param repo: repo's name
        :param key_id: key's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/keys/{key_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
