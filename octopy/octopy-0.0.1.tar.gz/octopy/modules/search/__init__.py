from octopy import request, model


class Search:

    """
    Official GITHUB documentation: https://developer.github.com/v3/search/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Search.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def repositories(self, text_match=False, page=1, **kwargs):
        """
        Returns all repositories filtered by given criteria.

        :kwarg page: from which page repos to be returned
        :kwarg q: [required] query, which must contain one or more search keywords
        :kwarg sort: sorts the results of the query.
            Can be `stars`, `forks`, or `help-wanted-issues`
        :kwarg order: Can be `asc`, or `desc`
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.mercy-preview+json"

        if text_match:
            headers["Accept"] = "application/vnd.github.v3.text-match+json"

        url = f"{self._url}/search/repositories?page={page}"
        items = [
            model.create_class("Repository", item)
            for item in request.get(url, headers=headers, params=kwargs)["items"]
        ]
        return items

    def commits(self, text_match=False, page=1, **kwargs):
        """
        Returns all commits filtered by a given criteria.

        :kwarg page: from which page results to be returned
        :kwarg q: [required] one or more keywords
        :kwarg sort: sort the result by `author-date`, or `committer-date`
        :kwarg order: can be `asc`, or `desc`
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.cloak-preview"

        if text_match:
            headers["Accept"] = "application/vnd.github.v3.text-match+json"

        url = f"{self._url}/search/commits?page={page}"
        items = [
            model.create_class("Commit", item)
            for item in request.get(url, headers=headers, params=kwargs)["items"]
        ]
        return items

    def code(self, text_match=False, page=1, **kwargs):
        """
        Returns all file contents, filtered by given criteria.

        :kwarg page: from which page, results to be returned; default: 1
        :kwarg q: [required] one or more keywords
        :kwarg sort: 
        :kwarg order: can be `asc`, or `desc`
        """
        headers = self._headers
        if text_match:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.v3.text-match+json"

        url = f"{self._url}/search/code?page={page}"
        items = [
            model.create_class("Code", item)
            for item in request.get(url, headers=headers, params=kwargs)["items"]
        ]
        return items

    def issues(self, text_match=False, page=1, **kwargs):
        """
        Returns all issues, filtered by a given criteria.

        :kwarg page: from which page, results to be returned; default: 1
        :kwarg q: [required] one or more keywords
        :kwarg order:
        :kwarg sort: can be `asc`, or `desc`
        """
        headers = self._headers
        if text_match:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.v3.text-match+json"

        url = f"{self._url}/search/issues?page={page}"
        items = [
            model.create_class("Issue", item)
            for item in request.get(url, headers=headers, params=kwargs)["items"]
        ]
        return items

    def users(self, text_match=False, page=1, **kwargs):
        """
        Returns all users, filtered by a given criteria.

        :kwarg page: from which page, results to be returned; default: 1
        :kwarg q: [required] one or more keywords
        :kwarg order: 
        :kwarg sort: can be `asc`, or `desc`
        """
        headers = self._headers
        if text_match:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.v3.text-match+json"

        url = f"{self._url}/search/users?page={page}"
        items = [
            model.create_class("User", item)
            for item in request.get(url, headers=headers, params=kwargs)["items"]
        ]
        return items

    def topics(self, text_match=False, page=1, **kwargs):
        """
        Returns all topics, filtered by a given criteria.

        :kwarg page: from which page, results to be returned
        :kwarg q: [required] one or more keywords
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.cloak-preview"

        if text_match:
            headers["Accept"] = "application/vnd.github.v3.text-match+json"

        url = f"{self._url}/search/topics?page={page}"
        items = [
            model.create_class("Topic", item)
            for item in request.get(url, headers=headers, params=kwargs)["items"]
        ]
        return items

    def labels(self, text_match=False, page=1, **kwargs):
        """
        Returns all labels, filtered by a given criteria.

        :kwarg page: from which page results to be returned; default: 1
        :kwarg repository_id: [required] repository's id
        :kwarg q: [required] one or more keywords
        :kwarg order: 
        :kwarg sort:
        """
        headers = self._headers
        if text_match:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.v3.text-match+json"

        url = f"{self._url}/search/labels?page={page}"
        items = [
            model.create_class("Label", item)
            for item in request.get(url, headers=headers, params=kwargs)["items"]
        ]
        return items
