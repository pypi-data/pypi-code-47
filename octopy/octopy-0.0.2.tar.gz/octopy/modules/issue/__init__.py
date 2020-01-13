from .assignee import Assignee
from .comment import Comment
from .event import Event
from .label import Label
from .milestone import Milestone
from .timeline import Timeline

from octopy import request, model


class Issue:

    """
    Official GITHUB documentation: https://developer.github.com/v3/issues/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Issue.md
    """

    def __init__(self, url, headers):
        self.assignees = Assignee(url, headers)
        self.comments = Comment(url, headers)
        self.events = Event(url, headers)
        self.labels = Label(url, headers)
        self.milestones = Milestone(url, headers)
        self.timeline = Timeline(url, headers)

        self._url = url
        self._headers = headers

    def all(
        self,
        page=1,
        user=False,
        org=None,
        performed_via_github_app=False,
        reactions=False,
        **kwargs,
    ):
        """
        Returns all issues of the authenticated user.

        :kwarg page: from which page, issues to be returned, default is 1
        :kwarg user: if set to true, it will return all issues across owner
            and member repositories, assignes to the authenticated user. default: false
        :kwarg org: if given, it will return all issues for an organization assigned
            to the authenticated user
        :kwarg performed_via_github_app:
        :kwarg reactions: if set to true, in the final result, reactions field will be included
        :kwarg filter: Indicates which sorts of issues to return. Can be one of:
            * assigned: Issues assigned to you
            * created: Issues created by you
            * mentioned: Issues mentioning you
            * subscribed: Issues you're subscribed to updates for
            * all: All issues the authenticated user can see, regardless of participation or creation
            Default: assigned
        :kwarg state: Indicates the state of 
            the issues to return. Can be either open, closed, or all. Default: open
        :kwarg labels: A list of comma separated label names. Example: bug,ui,@high
        :kwarg sort: What to sort results by. Can be either created, updated, comments. Default: created
        :kwarg direction: The direction of the sort. Can be either asc or desc. Default: desc
        :kwarg since: Only issues updated at or after this time are 
            returned. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        """
        headers = self._headers
        if performed_via_github_app or reactions:
            headers = headers.copy()

        if performed_via_github_app:
            headers["Accept"] = "application/vnd.github.machine-man-preview"
        elif reactions:
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        url = f"{self._url}/{f'user/' if user else f'orgs/{org}/' if org else ''}issues?page={page}"
        items = [
            model.create_class("Issue", item)
            for item in request.get(url, headers=headers, params=kwargs)
        ]
        return items

    def repository(
        self,
        owner,
        repo,
        page=1,
        performed_via_github_app=False,
        reactions=False,
        **kwargs,
    ):
        """
        Returns all issues for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page issues to be returned, default 1
        :kwarg performed_via_github:
        :kwarg milestone: If an integer is passed, it should refer to a milestone 
            by its number field. If the string * is passed, 
            issues with any milestone are accepted. 
            If the string none is passed, issues without milestones are returned.
        :kwarg state: Indicates the state of 
            the issues to return. Can be either open, closed, or all. Default: open
        :kwarg assignee: Can be the name of a user. 
            Pass in none for issues with no assigned 
            user, and * for issues assigned to any user.
        :kwarg creator: The user that created the issue.
        :kwarg mentioned: A user that's mentioned in the issue.
        :kwarg labels: A list of comma separated label names. Example: bug,ui,@high
        :kwarg sort: What to sort results by. 
            Can be either created, updated, comments. Default: created
        :kwarg direction: The direction of the sort. 
            Can be either asc or desc. Default: desc
        :kwarg since: Only issues updated at or after 
            this time are returned. This is a timestamp 
            in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        """
        headers = self._headers
        if performed_via_github_app or reactions:
            headers = headers.copy()

        if performed_via_github_app:
            headers["Accept"] = "application/vnd.github.machine-man-preview"
        elif reactions:
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        url = f"{self._url}/repos/{owner}/{repo}/issues?page={page}"
        items = [
            model.create_class("Issue", item)
            for item in request.get(url, headers=headers, params=kwargs)
        ]
        return items

    def get(self, owner, repo, issue_number, reactions=False):
        """
        Returns a single issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        :kwarg reactions: if set to true, the final result will include information about
            reactions
        """
        headers = self._headers
        if reactions:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.squirrel-girl-preview"

        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}"
        return model.create_class("Issue", request.get(url, headers=headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates an issue.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg title: [required] issue's title
        :kwarg body: content of the issue
        :kwarg milestone: the number of the milestone to associate this issue with
        :kwarg labels: list with labels
        :kwarg assignees: list with usernames to which the issue to be assigned
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues"
        return model.create_class(
            "Issue", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, issue_number, **kwargs):
        """
        Updates an issue.

        :param owner:
        :param repo:
        :param issue_numnber:
        :kwarg title: issue's title
        :kwarg body: content of the issue
        :kwarg state: issue's state, can be `open` or `closed`
        :kwarg milestone: the number of the milestone to associate this issue with
        :kwarg labels: list with labels
        :kwarg assignees: list with usernames to which the issue to be assigned
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}"
        return model.create_class(
            "Issue", request.patch(url, headers=headers, params=kwargs)
        )

    def lock(self, owner, repo, issue_number, **kwargs):
        """
        Locks an issue.

        :param owner: owner's name
        :param repo:  repo's name
        :param issue_number: issue's number
        :kwarg locked_reason: can be `off-topic`, `too heated`, `resolved`, or `spam`
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/lock"
        return request.put(url, headers=self._headers, params=kwargs)

    def unlock(self, owner, repo, issue_number):
        """
        Unlocks an issue.

        :param owner: owner's name
        :param repo: repo's name
        :param issue_number: issue's number
        """
        url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/lock"
        return request.delete(url, headers=self._headers)
