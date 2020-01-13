from octopy import request, model

from .branch import Branch
from .collaborator import Collaborator
from .comment import Comment
from .commit import Commit
from .community import Community
from .content import Content
from .deploy_key import DeployKey
from .deployment import Deployment
from .fork import Fork
from .invitation import Invitation
from .merge import Merge
from .page import Page
from .release import Release
from .statistic import Statistic
from .status import Status
from .traffic import Traffic
from .webhook import Webhook


class Repository:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

        self.branches = Branch(url, headers)
        self.collaborators = Collaborator(url, headers)
        self.comments = Comment(url, headers)
        self.commits = Commit(url, headers)
        self.community = Community(url, headers)
        self.contents = Content(url, headers)
        self.deploy_keys = DeployKey(url, headers)
        self.deployments = Deployment(url, headers)
        self.forks = Fork(url, headers)
        self.invitations = Invitation(url, headers)
        self.merges = Merge(url, headers)
        self.pages = Page(url, headers)
        self.releases = Release(url, headers)
        self.statistics = Statistic(url, headers)
        self.statuses = Status(url, headers)
        self.traffics = Traffic(url, headers)
        self.webhooks = Webhook(url, headers)

    def mine(self, page=1, topics=False, **kwargs):
        """
        Returns all repositories of the authenticated user.

        :kwarg page: from which page repositories to be returned
        :kwarg visibility: can be one of `all`, `public`, `private`; default: `all`
        :kwarg topics: 
        :kwarg affiliation: comma-separated list of valies. Can include:
            `owner`, `collaborator`, `organization_member`; default: `owner,collaborator,organization_member`
        :kwarg type: can be one of `all`, `owner`, `public`, `private`, `member`; default: `all`
        :kwarg sort: can be one of `created`, `updated`, `pushed`, `full_name`; default: `full_name`
        :kwarg direction: can be one `asc`, or `desc`; default: `asc` when using `fullname`, otherwise `desc`
        """
        url = f"{self._url}/user/repos?page={page}"
        items = [
            model.create_class("Repository", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def user(self, username, page=1, **kwargs):
        """
        Returns all repositories of auser.

        :param username: user's name
        :kwarg page: from which page repositories to be returned
        :kwarg type: can be one of `all`, `owner`, `member`; default: `owner`
        :kwarg sort: can be one of `created`, `updated`, `pushed`, `full_name`; default: `full_name`
        :kwarg direction: can be one of `asc`, or `desc`; default: `asc`, when using `full_name`, otherwise `desc`.
        """
        url = f"{self._url}/users/{username}/repos?page={page}"
        items = [
            model.create_class("Repository", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def organization(self, org, page=1, **kwargs):
        """
        Returns all repositories of an organization.

        :param org: org's name
        :kwarg page: from which page repositories to be returned
        :kwarg type: specifies the type of repositories returned. Can be
            one of `all`, `public`, `private`, `forks`, `sources`, `member`, `internal`;
            default: `all`
        :kwarg sort: can be one on `created`, `updated`, `pushed`, `full_name`
        :kwarg direction: can be one of `asc`, or `desc`; default: `asc` when using `full_name`,
            `desc` otherwise
        """
        url = f"{self._url}/orgs/{org}/repos?page={page}"
        items = [
            model.create_class("Repository", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def public(self, page=1, **kwargs):
        """
        Returns all public repositories.

        :kwarg page: from which page repositories to be returned
        :kwarg since: the ID of the last repository you've seen.
        """
        url = f"{self._url}/repositories?page={page}"
        items = [
            model.create_class("Repository", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def create(self, org=None, template=False, **kwargs):
        """
        Creates a new repository for the authenticated user, or a specific org.

        :kwarg org: if specified, the repository will be made
            in the given organization
        :kwarg template: if set to true, it will create
            a repository template

        Kwarg for org, or authenticated user /template is set to false/
        :kwarg name: [required] repository's name
        :kwarg description: short description of the repository
        :kwarg homepage: url for the repository
        :kwarg private: can be `true`, or `false`; default: `false`
        :kwarg visibility: can be `public`, or `private`
        :kwarg has_issues: if set to true, it will enable issues for this repository;
            default: `false`
        :kwarg has_projects: if set to true, it will enable projects for this repository;
            default: `false`
        :kwarg has_wiki: if set to true, it will enable `wiki` for this repository;
            default: `false`
        :kwarg is_template: if set to true, it will make this repository as a template
            repository
        :kwarg team_id: team's id to which an access will be granted
        :kwarg auto_init: creates an initial commit with empty README; default: `false`
        :kwarg gitignore_template: Desired language or platform 
            .gitignore template to apply. 
            Use the name of the template without 
            the extension. For example, "Haskell".
        :kwarg license_template: Choose an open source license 
            template that best suits your needs, and then use the license 
            keyword as the license_template string. For example, "mit" or "mpl-2.0".
        :kwarg allow_squash_merge:
            Either true to allow 
            squash-merging pull requests, or false to prevent squash-merging. Default: true
        :kwarg allow_merge_commit: Either true to allow merging 
            pull requests with a merge commit, or 
            false to prevent merging pull requests 
            with merge commits. Default: true
        :kwarg allow_rebase_merge: Either true to allow 
            rebase-merging pull requests, or 
            false to prevent rebase-merging. Default: true

        Kwargs when template is set to true
        :kwarg owner: owner's name
        :kwarg name: [required] name of the new repository
        :kwarg description: short description for the repository
        :kwarg private: specifies the access for the repo; default: `false`
        """
        if org:
            url = f"{self._url}/orgs/{org}/repos"
        elif template:
            template_owner = kwargs.get("template_owner")
            del kwargs["template_owner"]
            template_repo = kwargs.get("template_repo")
            del kwargs["template_repo"]
            url = f"{self._url}/repos/{template_owner}/{template_repo}/generate"
        else:
            url = f"{self._url}/user/repos"
        return model.create_class(
            "Repository", request.post(url, headers=self._headers, params=kwargs)
        )

    def get(self, owner, repo):
        """
        Returns a single repository.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}"
        return model.create_class("Repository", request.get(url, headers=self._headers))

    def update(self, owner, repo, **kwargs):
        """
        Updates a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg owner: owner's name
        :kwarg name: name of the repository
        :kwarg description: short description
        :kwarg homepage: url with more information about the repository
        :kwarg private: specifies the access to the repo; default: false
        :kwarg visibility: can be `public`, or `private`
        :kwarg has_issues: enables issues for this repository; default: false
        :kwarg has_projects: enables projects for this repository; default: false
        :kwarg has_wiki: enables wiki for this repository; default: true
        :kwarg is_template: makes this repository as template; default: true
        :kwarg default_branch: updates the default branch for this repository
        :kwarg allow_squach_merge: allows squach-mergins pull-requests; default: true
        :kwarg allow_merge_commit: allows mergins pull-requests; default: true
        :kwarg allow_rebase_merge: allows rebase-mergins; default: true
        :kwarg archived: archives the repository; default: false
        """
        url = f"{self._url}/repos/{owner}/{repo}"
        return model.create_class(
            "Repository", request.patch(url, headers=self._headers, params=kwargs)
        )

    def topics(self, owner, repo, topics=False):
        """
        Returns all topics for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg topics: if set to true, it will provide information about the topics; default: false
        """
        headers = self._headers
        if topics:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.mercy-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/topics"
        return model.create_class("Topics", request.get(url, headers=headers))

    def replace(self, owner, repo, topics=False, **kwargs):
        """
        Replaces all topics for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg topics: if set to true, it will provide information about the topics; default: false
        :kwarg names: list with topic names
        """
        headers = self._headers
        if topics:
            headers = headers.copy()
            headers["Accept"] = "application/vnd.github.mercy-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/topics"
        return model.create_class(
            "Topics", request.put(url, headers=headers, params=kwargs)
        )

    def vulnerability_alerts(self, owner, repo, ebanle=False, disable=False):
        """
        Gets or modifies vulnerability alerts.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg enable: if set to true it will enable them; default: false
        :kwarg disable: if set to true, it will disable them; default: false
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.dorian-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/vulnerability-alerts"
        if enable:
            return model.create_class("Status", request.put(url, headers=headers))
        elif disable:
            return model.create_class("Stauts", request.delete(url, headers=headers))
        else:
            return model.create_class("Status", request.get(url, headers=headers))
        raise TypeError("Invalid choice.")

    def automated_security_fixes(self, owner, repo, enable=False, disable=False):
        """
        Enables/Disables security fixes.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg enable: if set to true, enables automated security fixes; default: false
        :kwarg disable: if set to true, disables automated security fixes; default: false
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.london-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/automated-security-fixes"
        if enable:
            return model.create_class("Status", request.put(url, headers=headers))
        elif disable:
            return model.create_class("Status", request.delete(url, headers=headers))

        raise TypeError("Invalid option.")

    def contributors(self, owner, repo, page=1, **kwargs):
        """
        Returns all contributors for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page, contributors to be returned; default: 1
        :kwarg anon: if set to true, or 1, it will include anonimous contributors
            to the result; default: false
        """
        url = f"{self._url}/repos/{owner}/{repo}/contributors?page={page}"
        items = [
            model.create_class("Contributor", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def languages(self, owner, repo):
        """
        Returns all languages used in a repository.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}/languages"
        return model.create_class("Languages", request.get(url, headers=self._headers))

    def teams(self, owner, repo, page=1):
        """
        Returns all teams for a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page, teams to be returned; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/teams?page={page}"
        items = [
            model.create_class("Team", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def tags(self, owner, repo, page=1):
        """
        Returns all tags of a repository.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page, tags to be retuend; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/tags?page={page}"
        items = [
            model.create_class("Tag", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def remove(self, owner, repo):
        """
        Deletes a repository.

        :param owner: owner's name
        :param repo: repo's name
        """
        url = f"{self._url}/repos/{owner}/{repo}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def transfer(self, owner, repo, **kwargs):
        """
        Transfers a repository to a new owner.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg new_owner: [required] name of the new owner
        :kwarg team_ids: list with ids of the team/teams to add to the repository
        """
        url = f"{self._url}/repos/{owner}/{repo}/transfer"
        return model.create_class(
            "Repository", request.post(url, headers=self._headers, params=kwargs)
        )

    def create_dispatch_event(self, owner, repo, **kwargs):
        """
        Triggers a webhook event.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg event_type: [required] custom webhook event
        :kwarg client_payload: JSON payload with extra information about the webhook event.
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.everest-preview+json"

        url = f"{self._url}/repos/{owner}/{repo}/dispatches"
        return model.create_class(
            "Status", request.post(url, headers=headers, params=kwargs)
        )
