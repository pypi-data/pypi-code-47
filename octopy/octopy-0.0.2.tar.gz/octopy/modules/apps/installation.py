from octopy import request, model


class Installation:

    """
    Official documentation in Github: https://developer.github.com/v3/apps/installations/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/App-Installation.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.machine-man-preview+json"

    def repositories(self, page=1, topics=False):
        """
        Returns all repositories that an installation can access.

        :kwarg page: returns all repositories from the given page; default: 1
        :kwarg topics: if set to true, the final result will include information
            about topics
        """
        headers = self._headers
        if topics:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.mercy-preview+json"

        url = f"{self._url}/installation/repositories?page={page}"
        items = [
            model.create_class("Installation", item)
            for item in request.get(url, headers=self._headers)["repositories"]
        ]
        return items

    def user(self, page=1):
        """
        Returns all installations that an authenticated user can access.

        :kwarg page: returns all installations from the given page; default: 1
        """
        url = f"{self._url}/user/installations?page={page}"
        items = [
            model.create_class("Installation", item)
            for item in request.get(url, headers=self._headers)["installations"]
        ]
        return items

    def accessible(self, installation_id, page=1, topics=False):
        """
        Returns all installations accessible to the authenticated user.

        :param installation_id: installation's id
        :kwarg page: from which page installations to be returned
        :kwarg topics: specifies if the final result will include or not
            the topics property; default: false
        """
        headers = self._headers
        if topics:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.mercy-preview+json"

        url = (
            f"{self._url}/user/installations/{installation_id}/repositories?page={page}"
        )
        items = [
            model.create_class("Installation", item)
            for item in request.get(url, headers=self._headers)["repositories"]
        ]
        return items

    def create(self, installation_id, repository_id):
        """
        Adds a repository for installation.

        :param installation_id: installation's id
        :param repository_id: repository's id
        """
        url = f"{self._url}/user/installations/{installation_id}/repositories/{repository_id}"
        return model.create_class("Status", request.put(url, headers=self._headers))

    def remove(self, installation_id, repository_id):
        """
        Removes a repository for installation.

        :param installation_id: installation's id
        :param repository_id: repository's id
        """
        url = f"{self._url}/user/installations/{installation_id}/repositories/{repository_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def create_content_attachment(self, content_reference_id, **kwargs):
        """
        Creates an attachment under a content 
            reference URL in the body or comment of an issue or pull request.

        :param content_reference_id: content reference's id
        :kwarg title: [required] title of the content attachment
        :kwarg body: [required] text of the content attachment
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.corsair-preview+json"
        url = f"{self._url}/content_references/{content_reference_id}/attachments"
        return model.create_class(
            "ContentAttachment", request.post(url, headers=headers, params=kwargs)
        )
