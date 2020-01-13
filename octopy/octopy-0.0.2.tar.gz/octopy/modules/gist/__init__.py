from .comment import Comment
from octopy import request, model


class Gist:
    def __init__(self, url, headers):
        self.comments = Comment(url, headers)
        self._url = url
        self._headers = headers

    def user(self, username, page=1, **kwargs):
        """
        Returns all gists of a given user.

        :param username: user's name
        :kwarg page: from which page, gists to be returned; default: 1
        :kwarg since: from when gists to be returned
        """
        url = f"{self._url}/users/{username}/gists?page={page}"
        items = [
            model.create_class("Gist", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def mine(self, page=1, **kwargs):
        """
        Returns all gists of the authenticated user.

        :kwarg page: from which page, gists to be retuend; default: 1.
        :kwarg since: from when gists to be returned
        """
        url = f"{self._url}/gists?page={page}"
        items = [
            model.create_class("Gist", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def all(self, page=1, **kwargs):
        """
        Returns all public gists.

        :kwarg page: from which page, gists to be retuend; default: 1.
        :kwarg since: from when gists to be returned
        """
        url = f"{self._url}/gists/public?page={page}"
        items = [
            model.create_class("Gist", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def starred(self, page=1, **kwargs):
        """
        Returns all user's starred gists.

        :kwarg page: from which page, gists to be retuend; default: 1.
        :kwarg since: from when gists to be returned
        """
        url = f"{self._url}/gists/starred?page={page}"
        items = [
            model.create_class("Gist", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def get(self, gist_id):
        """
        Returns a single gist.

        :param gist_id: gist's id
        """
        url = f"{self._url}/gists/{gist_id}"
        return model.create_class("Gist", request.get(url, headers=self._headers))

    def revision(self, gist_id, sha):
        """
        Returns a specific revision of a gist.

        :param gist_id: gist's id
        :param sha:
        """
        url = f"{self._url}/gists/{gist_id}/{sha}"
        return model.create_class("Gist", request.get(url, headers=self._headers))

    def create(self, **kwargs):
        """
        Creates a gist.

        :kwarg files: [required] filenames and content of each file in the gist
            :kwarg content: content of the file
        :kwarg description: name of the gist
        :kwarg public: if set to true, everyone can see it; default: false
        """
        url = f"{self._url}/gists"
        return model.create_class(
            "Gist", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, gist_id, **kwargs):
        """
        Updates a gist.

        :param gist_id: gist's id
        :kwarg description: gist's name
        :kwarg files:
            :kwarg content: updated content of the file
            :kwarg filename: ne name of this file
        """
        url = f"{self._url}/gists/{gist_id}"
        return model.create_class(
            "Gist", request.patch(url, headers=self._headers, params=kwargs)
        )

    def commits(self, gist_id, page=1):
        """
        Returns all commits to a given gist.

        :param gist_id: gist's id
        :kwarg page: returns all commits from a given page; default: 1
        """
        url = f"{self._url}/gists/{gist_id}/commits?page={page}"
        items = [
            model.create_class("Commit", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def star(self, gist_id):
        """
        Stars a gist.

        :param gist_id: gist's id
        """
        url = f"{self._url}/gists/{gist_id}/star"
        return model.create_class("Stauts", request.put(url, headers=self._headers))

    def unstar(self, gist_id):
        """
        Unstars a gist.

        :param gist_id: gist's id
        """
        url = f"{self._url}/gists/{gist_id}/star"
        return model.create_class("Stauts", request.delete(url, headers=self._headers))

    def starred(self, gist_id):
        """
        Returns information if a gist is starred.

        :param gist_id: gist's id
        """
        url = f"{self._url}/gists/{gist_id}/star"
        return model.create_class("Stauts", request.get(url, headers=self._headers))

    def fork(self, gist_id):
        """
        Forks a gist.

        :param gist_id: gist's id
        """
        url = f"{self._url}/gists/{gist_id}/forks"
        return model.create_class("Fork", request.post(url, headers=self._headers))

    def forks(self, gist_id, page=1):
        """
        Returns all forks of a gist.

        :param gist_id: gist's id
        :kwarg page: from which page, forks to be returned; default: 1
        """
        url = f"{self._url}/gists/{gist_id}/forks?page={page}"
        items = [
            model.create_class("Fork", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def remove(self, gist_id):
        """
        Deletes a gist.

        :param gist_id: gist's id
        """
        url = f"{self._url}/gists/{gist_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
