from octopy import request, model


class Follower:

    """
    Official GITHUB documentation: https://developer.github.com/v3/users/followers/#list-users-followed-by-another-user
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/UserFollowers.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def user(self, username, page=1):
        """
        Returns all user's followers.

        :param username: user's name
        :kwarg page: from which page, followers to be returned
        """
        url = f"{self._url}/users/{username}/followers?page={page}"
        items = [
            model.create_class("Follower", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def mine(self, page=1):
        """
        Returns all followers of the currently authenticated user.

        :kwarg page: from which page, followers to be returned; default: 1
        """
        url = f"{self._url}/user/followers?page={page}"
        items = [
            model.create_class("Follower", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def following(self, username, page=1):
        """
        Returns user's following list.

        :param username: user's name
        :kwarg page: from which page users to be returned
        """
        url = f"{self._url}/users/{username}/following?page={page}"
        items = [
            model.create_class("Following", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def my_followings(self, page=1):
        """
        Returns authenticated user's following list.

        :kwarg page: from which page, results to be returned; default: 1
        """
        url = f"{self._url}/user/following?page={page}"
        items = [
            model.create_class("Following", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def am_i_following(self, username):
        """
        Checks if currently authenticated user is following a user.

        :param username: user's name
        """
        url = f"{self._url}/user/following/{username}"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def follows(self, username, target_user):
        """
        Checks if a user is following another user.

        :param username: user's name 
        :param target_user: other user's name
        """
        url = f"{self._url}/users/{username}/following/{target_user}"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def follow(self, username):
        """
        Follows a user.

        :param username: user's name to follow
        """
        url = f"{self._url}/user/following/{username}"
        return model.create_class("Status", request.put(url, headers=self._headers))

    def unfollow(self, username):
        """
        Unfollows a user.

        :param username: user's name to unfollow
        """
        url = f"{self._url}/user/following/{username}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
