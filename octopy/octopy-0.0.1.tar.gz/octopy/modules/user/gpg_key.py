from octopy import request, model


class GPGKey:

    """
    Official GITHUB documentation: https://developer.github.com/v3/users/gpg_keys/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/UserGPGKeys.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def user(self, username, page=1):
        """
        Returns all user's GPG keys.

        :param username: user's name
        :kwarg page: from which page results to be returned; default: 1
        """
        url = f"{self._url}/users/{username}/gpg_keys?page={page}"
        items = [
            model.create_class("GPGKey", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def mine(self, page=1):
        """
        Returns all GPG keys of currently authenticated user.

        :kwarg page: from which page results to be returned; default: 1
        """
        url = f"{self._url}/users/gpg_keys?page={page}"
        items = [
            model.create_class("GPGKey", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, gpg_key_id):
        """
        Returns a single GPG key.

        :param gpg_key_id: gpg key's id
        """
        url = f"{self._url}/user/gpg_keys/{gpg_key_id}"
        return model.create_class("GPGKey", request.get(url, headers=self._headers))

    def create(self, **kwargs):
        """
        Creates a GPG key.

        :kwarg armored_public_key: Your GPG key, generated in ASCII-armored format. 
            See "Generating a new GPG key"(https://help.github.com/articles/generating-a-new-gpg-key/) for help creating a GPG key.
        """
        url = f"{self._url}/user/gpg_keys"
        return model.create_class(
            "GPGKey", request.post(url, headers=self._headers, params=kwargs)
        )

    def remove(self, gpg_key_id):
        """
        Deletes a gpg key.

        :param gpg_key_id: gpg key's id
        """
        url = f"{self._url}/user/gpg_keys/{gpg_key_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
