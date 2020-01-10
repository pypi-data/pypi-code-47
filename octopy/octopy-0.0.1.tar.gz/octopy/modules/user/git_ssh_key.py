from octopy import request, model


class GitSshKey:

    """
    Official GITHUB documentation: 
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/UserGitSHHKey.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def public_keys(self, username, page=1):
        """
        Returns all public keys for a user.

        :param username: user's name
        :param page: from which page, results to be returned; default: 1
        """
        url = f"{self._url}/users/{username}/keys?page={page}"
        items = [
            model.create_class("GitSshKey", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def mine(self, page=1):
        """
        Returns all keys of the currently authenticated user.

        :kwarg page: from which page, keys to be returned; default: 1
        """
        url = f"{self._url}/users/keys?page={page}"
        items = [
            model.create_class("GitSshKey", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, key_id):
        """
        Returns a single public key.

        :param key_id: key's id
        """
        url = f"{self._url}/user/keys/{key_id}"
        return model.create_class("GitSshKey", request.get(url, headers=self._headers))

    def create(self, **kwargs):
        """
        Creates a public key.

        :kwarg title: name for the new key.
        :kwarg key: The public SSH key to add to your GitHub account. 
            See "Generating a new SSH key"(https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) 
            for guidance on how to create a public SSH key.
        """
        url = f"{self._url}/user/keys"
        return model.create_class(
            "GitSshKey", request.post(url, headers=self._headers, params=kwargs)
        )

    def remove(self, key_id):
        """
        Deletes a key.

        :param key_id: key's id
        """
        url = f"{self._url}/user/keys/{key_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
