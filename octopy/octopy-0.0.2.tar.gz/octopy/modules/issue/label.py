from octopy import request, model


class Label:

    """
    Official GITHUB documentation: https://developer.github.com/v3/issues/labels/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Issue-Label.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1):
        """
        Returns all label for a given repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page labels to be returned
        """
        url = f"{self._url}/repos/{owner}/{repo}/labels?page={page}"
        items = [
            model.create_class("Label", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, owner, repo, name):
        """
        Returns a single label.

        :param owner: owner's name
        :param repo: repo's name
        :param name: label's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/labels/{name}"
        return model.create_class("Label", request.get(url, headers=self._headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates a label.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg name: label's name
        :kwarg color: label's color
        :kwarg description: label's description
        """
        url = f"{self._url}/repos/{owner}/{repo}/labels"
        return model.create_class(
            "Label", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, name, **kwargs):
        """
        Updates a label.

        :param owner: owner's name
        :param repo: repo's name
        :param name: label's name
        :kwarg new_name: label's new name
        :kwarg description: label's description
        :kwarg color: label's color
        """
        url = f"{self._url}/repos/{owner}/{repo}/labels/{name}"
        return model.create_class(
            "Label", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, name):
        """
        Deletes a label.

        :param owner: owner's name
        :param repo: repo's name
        :param name: label's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/labels/{name}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def issue(self, owner, repo, issue_number, page=1):
        """
        Returns all labels of an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg page: from which page results to be returned, default: 1
        """
        url = (
            f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/labels?page={page}"
        )
        items = [
            model.create_class("IssueLabel", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def create_issue_label(self, owner, repo, issue_number, **kwargs):
        """
        Creates a label to an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg labels: [required] list with names for the label
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/labels"
        items = [
            model.create_class("IssueLabel", item)
            for item in request.post(url, headers=self._headers, params=kwargs)
        ]
        return items

    def replace_issue_labels(self, owner, repo, issue_number, **kwargs):
        """
        Replaces all labels of an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg labels: list with new label names
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/labels"
        items = [
            model.create_class("IssueLabel", item)
            for item in request.put(url, headers=self._headers)
        ]
        return items

    def remove_issue_labels(self, owner, repo, issue_number, name=None):
        """
        Removes one or all labels from an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg name: if given, it will remove only the given label.
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/labels{f'{name}' if name else ''}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def milestone(self, owner, repo, milestone_number, page=1):
        """
        Returns all labels for every issue in a milestone.

        :param owner: owner's name
        :param repo: repo's name
        :param milestone_number: milestone's number
        :kwarg page: from which page labels to be returned, default: 1
        """
        url = f"{self._url} /repos/{owner}/{repo}/milestones/{milestone_number}/labels?page={page}"
        items = [
            model.create_class("IssueLabel", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items
