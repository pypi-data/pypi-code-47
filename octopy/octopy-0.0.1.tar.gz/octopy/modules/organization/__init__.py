from .blocking_user import BlockingUser
from .member import Member
from .outside_collaborator import OutsideCollaborator
from .webhook import Webhook

from octopy import request, model


class Organization:

    """
    Official GITHUB documentation: https://developer.github.com/v3/orgs/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Organizations.md
    """

    def __init__(self, url, headers):
        self.blocking_users = BlockingUser(url, headers)
        self.members = Member(url, headers)
        self.outside_collaborators = OutsideCollaborator(url, headers)
        self.webhooks = Webhook(url, headers)

        self._url = url
        self._headers = headers

    def mine(self, page=1):
        """
        Returns all organizations of the current user.

        :kwarg page: from which page, orgs to be returned, default: 1
        """
        url = f"{self._url}/user/orgs?page={page}"
        items = [
            model.create_class("Organization", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def all(self, page=1):
        """
        Returns all organizations, sorted by their creation date.

        :kwarg page: from which page orgs to be returned, default: 1
        """
        url = f"{self._url}/organizations?page={page}"
        items = [
            model.create_class("Organization", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def user(self, username, page=1):
        """
        Returns all user's organizations.

        :param username: user's name
        :kwarg page: from which page orgs to be returned, default: 1
        """
        url = f"{self._url}/users/{username}/orgs?page={page}"
        items = [
            model.create_class("Organization", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def installations(self, org, page=1):
        """
        Returns all apps of an organization.

        :param org: org's name
        :kwarg page: from which page apps to be returned, default: 1
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.machine-man-preview+json"

        url = f"{self._url}/orgs/{org}/installations?page={page}"

        items = [
            model.create_class("Installation", item)
            for item in request.get(url, headers=headers)["installations"]
        ]
        return items

    def get(self, org):
        """
        Returns a single organization.

        :param org: org's name
        """
        headers = self._headers.copy()
        headers["Accept"] = "application/vnd.github.surtur-preview+json"

        url = f"{self._url}/orgs/{org}"
        return model.create_class("Organization", request.get(url, headers=headers))

    def update(self, org, **kwargs):
        """
        Updates an organization.

        :param org: org's name
        :kwarg billing_email: Billing email address. This address is not publicized.
        :kwarg company: company's name
        :kwarg email: public email address
        :kwarg location: location
        :kwarg name: shorthand company's name
        :kwarg description: description of the company
        :kwarg has_organization_projects: whether an organization
            can use organization projects
        :kwarg has_repository_projects: toggles whether repositories 
            that belong to the organization can use repository projects.
        :kwarg default_repository_permission: Default permission 
            level members have for organization repositories:
            * read - can pull, but not push to or administer this repository.
            * write - can pull and push, but not administer this repository.
            * admin - can pull, push, and administer this repository.
            * none - no permissions granted by default.
            Default: read
        :kwarg members_can_create_repositories: Toggles the 
            ability of non-admin organization members to create repositories. Can be one of:
                * true - all organization members can create repositories.
                * false - only organization owners can create repositories.
            Default: true
            Note: A parameter can override this parameter. 
            See members_allowed_repository_creation_type in this table for details.
        :kwarg members_can_create_internal_repositories: Toggles whether 
            organization members can create internal repositories, which are visible to all enterprise members. You can only allow members to create internal repositories if your organization is associated with an enterprise account using GitHub Enterprise Cloud. Can be one of:
                * true - all organization members can create internal repositories.
                * false - only organization owners can create internal repositories.
            Default: true. For more information, 
            see "Restricting repository creation in your organization" 
            in the GitHub Help documentation.
        :kwarg members_can_create_private_repositories: Toggles whether organization members 
            can create private repositories, which are visible to organization members with permission. Can be one of:
                * true - all organization members can create private repositories.
                * false - only organization owners can create private repositories.
            Default: true. For more information, 
            see "Restricting repository creation in your organization" 
            in the GitHub Help documentation.
        :kwarg members_can_create_public_repositories: Toggles whether organization members can create public repositories, which are visible to anyone. Can be one of:
            * true - all organization members can create public repositories.
            * false - only organization owners can create public repositories.
            Default: true. For more information, 
            see "Restricting repository creation in your organization" 
            in the GitHub Help documentation.
        :kwarg members_allowed_repository_creation_type: Specifies which types 
            of repositories non-admin organization members can create. Can be one of:
            * all - all organization members can create public and private repositories.
            * private - members can create private repositories. 
            This option is only available to repositories that are 
            part of an organization on GitHub Enterprise Cloud.
            * none - only admin members can create repositories.
            Note: This parameter is deprecated and will be 
            removed in the future. Its return value ignores internal 
            repositories. Using this parameter overrides values set 
            in members_can_create_repositories. See this note for details.
        """
        url = f"{self._url}/orgs/{org}"
        return model.create_class(
            "Organization", request.patch(url, headers=self._headers, params=kwargs)
        )

    def credential_authorizations(self, org):
        """
        Returns all credential authorizations for an org.

        :param org: org's name
        """
        url = f"{self._url}/orgs/{org}/credential-authorizations"
        items = [
            model.create_class("CredentialAuthorization", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def remove_credential_authorization(self, org, credential_id):
        """
        Removes a credential's authorization for an org.

        :param org: org's name
        :param credential_id: credential's id
        """
        url = f"{self._url}/orgs/{org}/credential-authorizations/{credential_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
