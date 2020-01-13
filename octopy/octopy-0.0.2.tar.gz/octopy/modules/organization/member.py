from octopy import request, model


class Member:

    """
    Official GITHUB documentation: https://developer.github.com/v3/orgs/members/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Organizations-Members.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, org, public=False, page=1, **kwargs):
        """
        Returns all members of an organization.

        :param org: org's name
        :kwarg page: from which page users to be returned, default: 1
        :kwarg filter: filters members returned in the list. 
            Can be `2fa_disabled`, or `all`, default: `all`
        :kwarg role: filters members by their role.
            Can be `all`(default), `admin`, `member`
        """
        url = f"{self._url}/orgs/{org}/{'public_members' if public else 'members'}?page={page}"
        items = [
            model.create_class("Member", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def check(self, org, username, public=False):
        """
        Checks if a user is member of an org.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/{'public_members' if public else 'members'}/{username}"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def remove(self, org, username):
        """
        Removes a user from an org.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/members/{username}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def publicize(self, org, username):
        """
        Makes username a public member of an org.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/public_members/{username}"
        return request.put(url, headers=self._headers)

    def hide(self, org, username):
        """
        Hides username from an org's member list.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/public_members/{username}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def membership(self, org, username):
        """
        Returns user's membersip of an org.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/memberships/{username}"
        return model.create_class("Status", request.get(url, headers=self._headers))

    def update(self, org, username, **kwargs):
        """
        Updates/Creates user's membership.

        :param org: org's name
        :param username: user's name
        :kwarg role: user's role
        """
        url = f"{self._url}/orgs/{org}/memberships/{username}"
        return model.create_class(
            "Membership", request.put(url, headers=self._headers, params=kwargs)
        )

    def remove(self, org, username):
        """
        Removes a user from an org.

        :param org: org's name
        :param username: user's name
        """
        url = f"{self._url}/orgs/{org}/memberships/{username}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def invitation_teams(self, org, invitation_id, page=1):
        """
        Returns all organization invitation teams.

        :param org: org's name
        :param ivtitation_id: invitation's id
        :kwarg page: from which page teams to be returned, default: 1
        """
        url = f"{self._url}/orgs/{org}/invitations/{invitation_id}/teams?page={page}"
        items = [
            model.create_class("InvitationTeam", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def pending_invitations(self, org, page=1):
        """
        Returns all pending invtiations from an org.

        :param org: org's name
        :kwarg page: from which page invitations to be returned, default: 1
        """
        url = f"{self._url}/orgs/{org}/invitations?page={page}"
        items = [
            model.create_class("PendingInvitation", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def invite(self, org, **kwargs):
        """
        Invites users to an org.

        :param org: org's name
        :kwarg invitee_id: user's id
        :kwarg email: user's email
        :kwarg role: user's role
        :kwarg team_ids: team ids
        """
        url = f"{self._url}/orgs/{org}/invitations"
        return model.create_class(
            "Invitation", request.post(url, headers=self._headers, params=kwargs)
        )

    def mine(self, org=False, page=1, **kwargs):
        """

        """
        url = f"{self._url}/user/memberships/orgs?page={page}"
        items = [
            model.create_class("Membership", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def update_membership(self, org, **kwargs):
        """

        """
        url = f"{self._url}/user/memberships/orgs/{org}"
        return model.create_class(
            "OrgMembership", request.patch(url, header=self._headers, params=kwargs)
        )
