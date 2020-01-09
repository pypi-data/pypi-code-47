import requests
from bbdata.config import output_api_url
from bbdata.util import handle_response

class ObjectGroups:

    base_path = "/objectGroups"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get_all(self, with_objects=False, writable=False):
        """
        Get the list of object groups accessible (in read-only) by the user.

        GET /objectGroups
        https://bbdata.daplab.ch/api/#objectgroups_get
        """
        params = {
            "withObjects": with_objects,
            "writable": writable,
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def put(self, name, unit_symbol, owner, description=None):
        """
        Create a new object group. To allow non-administrative group members
        to access it, don't forget to add permissions.

        PUT /objectGroups
        https://bbdata.daplab.ch/api/#objectgroups_put
        """
        data = {
            "name": name,
            "description": description,
            "unitSymbol": unit_symbol,
            "owner": str(owner),
        }
        url = output_api_url + self.base_path
        r = requests.put(url, data, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def get(self, group_id):
        """
        Get an object group with all its objects.

        GET /objectGroups/{groupId}
        https://bbdata.daplab.ch/api/#objectgroups__groupid__get
        """
        url = output_api_url + self.base_path + "/" + str(group_id)
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def post(self, group_id, data):
        """
        Edit the name and/or the description of the object group.
        Only the properties appearing in the body will be modified.

        POST /objectGroups/{groupId}
        https://bbdata.daplab.ch/api/#objectgroups__groupid__post
        """
        # TODO The data to send isn't define in the API Docs
        url = output_api_url + self.base_path + "/" + str(group_id)
        r = requests.post(url, data, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def delete(self, group_id):
        """
        Delete the object.

        DELETE /objectGroups/{groupId}
        https://bbdata.daplab.ch/api/#objectgroups__groupid__delete
        """
        url = output_api_url + self.base_path + "/" + str(group_id)
        r = requests.delete(url, headers=self.auth.headers)
        handle_response(r.status_code, True)

    def get_objects(self, group_id):
        """
        Get the list of objects part of the group.

        GET /objectGroups/{groupId}/objects
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_get
        """
        url = output_api_url + self.base_path + "/" + str(group_id) + "/objects"
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def put_object(self, group_id, object_id):
        """
        Add an object to the group.

        GET /objectGroups/{groupId}/objects
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_put
        """
        data = {
            "objectId": str(object_id),
        }
        url = output_api_url + self.base_path + "/" + str(group_id) + "/objects"
        r = requests.put(url, data, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def delete_object(self, group_id, object_id):
        """
        Delete the object.

        DELETE /objectGroups/{groupId}/objects
        https://bbdata.daplab.ch/api/#objectgroups__groupid__delete
        """
        data = {
            "objectId": str(object_id),
        }
        url = output_api_url + self.base_path + "/" + str(group_id) + "/objects"
        r = requests.delete(url, data, headers=self.auth.headers)
        return handle_response(r.status_code, True)

    def get_permissions(self, group_id):
        """
        Get the list of user group which have access to the group

        GET /objectGroups/{groupId}/permissions
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_put
        """
        url = output_api_url + self.base_path + "/" + str(group_id) + "/permissions"
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def put_permissions(self, group_id, group_id_to_add):
        """
        Grant permissions on the group to a user group.

        PUT /objectGroups/{groupId}/permissions
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_put
        """
        data = {
            "groupId": str(group_id_to_add),
        }
        url = output_api_url + self.base_path + "/" + str(group_id) + "/permissions"
        r = requests.put(url, data, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def delete_permissions(self, group_id, group_id_to_delete):
        """
        Revoke a permission.

        DELETE /objectGroups/{groupId}/permissions
        https://bbdata.daplab.ch/api/#objectgroups__groupid__objects_delete
        """
        data = {
            "groupId": str(group_id_to_delete),
        }
        url = output_api_url + self.base_path + "/" + str(group_id) + "/permissions"
        r = requests.delete(url, data, headers=self.auth.headers)
        return handle_response(r.status_code, True)



