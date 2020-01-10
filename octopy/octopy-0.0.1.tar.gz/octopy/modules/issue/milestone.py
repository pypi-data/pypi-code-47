from octopy import request, model


class Milestone:

    """
    Official GITHUB documentation: https://developer.github.com/v3/issues/milestones/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Issue-Milestone.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1, **kwargs):
        """
        Returns all milestones for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page milestones to be returned, default: 1
        :kwarg state: can be `open`, `closed`, or `all`, default: `open`
        :kwarg sort: can be `due_on`, or `completeness`, default: `due_on`
        :kwarg direction: can be `asc` or `desc`, default: `asc`
        """
        url = f"{self._url}/repos/{owner}/{repo}/milestones?page={page}"
        items = [
            model.create_class("Repository", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def get(self, owner, repo, milestone_number):
        """
        Returns a single milestone.

        :param owner: owner's name
        :param repo: repo's name
        :param milestone_number: milestone's number
        """
        url = f"{self._url}/repos/{owner}/{repo}/milestones/{milestone_number}"
        return model.create_class("Milestone", request.get(url, headers=self._headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates a milestone.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg title: [required] milestone's title
        :kwarg state: milestone's state
        :kwarg description: milestone's description
        :kwarg due_on: The milestone due date. 
        This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        """
        url = f"{self._url}/repos/{owner}/{repo}/milestones"
        return model.create_class(
            "Milestone", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, milestone_number, **kwargs):
        """
        Updates a milestone.

        :param owner: owner's name
        :param repo: repo's name
        :param milestone_number: milestone's number
        :kwarg title: milestone's title
        :kwarg state: milestone's state
        :kwarg description: milestone's description
        :kwarg due_on: The milestone due date. 
        This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        """
        url = f"{self._url}/repos/{owner}/{repo}/milestones/{milestone_number}"
        return model.create_class(
            "Milestone", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, owner, repo, milestone_number):
        """
        Deletes a milestone.

        :param owner: owner's name
        :param repo: repo's name
        :param milestone_number: milestone's number
        """
        url = f"{self._url}/repos/{owner}/{repo}/milestones/{milestone_number}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
