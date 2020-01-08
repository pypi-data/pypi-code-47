import requests
from bbdata.config import output_api_url
from bbdata.util import handle_non_ok_status, handle_response


class UserGroups:

    base_path = "/userGroups"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get_all(self, admin=False):
        """
        Get the list of all user groups.

        GET /userGroups
        https://bbdata.daplab.ch/api/#usergroups_get
        """
        params = {
            "admin": admin
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        print(url)
        return handle_response(r.status_code, r.json())

    def put(self, name):
        """
        Create a new user group. Upon success, you will automatically
        be promoted administrator of the new group.

        GET /userGroups
        https://bbdata.daplab.ch/api/#usergroups_put
        """
        if len(name) < 3 or len(name) > 50:
            raise ValueError
        data = {
          "name": name
        }
        url = output_api_url + self.base_path
        r = requests.put(url, data, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def delete(self, user_group_id):
        """
        Delete the user group. Note that you cannot delete a group which
        still has users.

        GET /userGroups
        https://bbdata.daplab.ch/api/#usergroups_delete
        """
        url = output_api_url + self.base_path
        r = requests.delete(url, headers=self.auth.headers)
        return handle_non_ok_status(r.status_code)

    def get(self, user_group_id):
        """
        Get a user group, including the list of its users.

        GET /userGroups/{userGroupId}
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__get
        """
        url = output_api_url + self.base_path + "/" + str(user_group_id)
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def get_users(self, user_group_id):
        """
        Get the list of users part of this group, with their access level
        (administrator or regular user).

        GET /userGroups/{userGroupId}/users
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__users_get
        """
        url = output_api_url + self.base_path + "/" + str(user_group_id) \
            + "/users"
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def put_users(self, user_group_id, user_id, is_admin=False):
        """
        Add a new user to the group. If the user already exists,
        but the access level specified in the request is different,
        it will be updated.

        GET /userGroups/{userGroupId}/users
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__users_put
        """
        params = {
            "userId": user_id,
            "isAdmin": is_admin
        }
        url = output_api_url + self.base_path + "/" + str(user_group_id) \
            + "/users"
        r = requests.put(url, params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def delete_users(self, user_group_id, user_id):
        """
        Remove a user from the group. Beware: if no administrator is left,
        objects belonging to this group won't be editable anymore.

        GET /userGroups/{userGroupId}/users
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__users_delete
        """
        params = {
            "userId": user_id,
        }
        url = output_api_url + self.base_path + "/" + str(user_group_id) \
            + "/users"
        r = requests.delete(url, params, headers=self.auth.headers)
        return handle_non_ok_status(r.status_code)

    def put_users_new(self, user_group_id, name, email, password, admin=False):
        """
        Create a new user and add it to the group.

        PUT /userGroups/{userGroupsId}/users/new
        https://bbdata.daplab.ch/api/#usergroups__usergroupid__users_new_put
        """
        params = {
            "admin": admin
        }
        data = {
            "name": name,
            "email": email,
            "password": password
        }
        url = output_api_url + self.base_path + "/" + str(user_group_id) \
            + "/users/new"
        r = requests.put(url, data, params=params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())
