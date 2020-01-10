from .blocking_user import BlockingUser
from .email import Email
from .follower import Follower
from .git_ssh_key import GitSshKey
from .gpg_key import GPGKey

from octopy import request, model


class User:

    """
    Official GITHUB documentation: 
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Users.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

        self.blocking_users = blocking_user.BlockingUser(url, headers)
        self.emails = email.Email(url, headers)
        self.followers = follower.Follower(url, headers)
        self.git_ssh_keys = git_ssh_key.GitSshKey(url, headers)
        self.gpg_keys = gpg_key.GPGKey(url, headers)

    def get(self, username):
        """
        Returns a single user.

        :param username: user's name
        """
        url = f"{self._url}/users/{username}"
        return model.create_class("User", request.get(url, headers=self._headers))

    def me(self):
        """
        Returns currently authenticated user.
        """
        url = f"{self._url}/user"
        return model.create_class("User", request.get(url, headers=self._headers))

    def update(self, **kwargs):
        """
        Updates a user.

        :kwarg name: new name of the user
        :kwarg email: publicly visible email
        :kwarg blog: new blog url of the use
        :kwarg company: new company of the user
        :kwarg location: new location of the user
        :kwarg hireable: new hiring availability of the user
        :kwarg bio: new short bio of the user
        """
        url = f"{self._url}/user"
        return model.create_class(
            "User",
            request.patch(
                url, request.patch(url, headers=self._headers, params=kwargs)
            ),
        )

    def info(self, username, **kwargs):
        """
        Returns contextual information about a user.

        :param username: user's name
        :kwarg subject_type: identifies the additional infomration
            you'd like to receive about the person's hovercard
        :kwart subject_id: uses the ID for the subject type you specified,
            and is required when using subject type
        """
        url = f"{self._url}/users/{username}/hovercard"
        return model.create_class(
            "User", request.get(url, headers=self._headers, params=kwargs)
        )

    def all(self, **kwargs):
        """
        Returns all users.

        :param since: ID of the last user you have seen.
        """
        url = f"{self._url}/users"
        items = [
            model.create_class("User", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items
