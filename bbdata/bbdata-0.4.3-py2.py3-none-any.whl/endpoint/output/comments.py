import requests
from bbdata.config import output_api_url
from bbdata.util import handle_response, handle_non_ok_status


class Comments:

    base_path = "/comments"
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get_all(self, object_ids=None):
        """
        Get all comments from objects you have read access to.

        GET /comments
        https://bbdata.daplab.ch/api/#comments_get
        """
        params = {
            "objectIds": object_ids
        }
        url = output_api_url + self.base_path
        r = requests.get(url, params, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def put(self, comment_id, object_id, from_datetime, to_datetime, comment):
        """
        Add a comment attached to an object.

        PUT /comments
        https://bbdata.daplab.ch/api/#comments_put
        """
        # TODO What is the diff between id and objectId? (comment id and obj id)
        #    and I think the comment could be clearer

        data = {
            "id": comment_id,
            "objectId": object_id,
            "from": from_datetime,
            "to": to_datetime,
            "comment": comment
        }
        url = output_api_url + self.base_path
        r = requests.put(url, data=data, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def get(self, comment_id):
        """
        Get one comment.

        GET /comments/{id}
        https://bbdata.daplab.ch/api/#comments__id__get
        """
        url = output_api_url + self.base_path + "/" + str(comment_id)
        r = requests.get(url, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())

    def delete(self, comment_id):
        """
        Delete a comment.

        DELETE /comments/{id}
        https://bbdata.daplab.ch/api/#comments__id__delete
        """
        url = output_api_url + self.base_path + "/" + str(comment_id)
        r = requests.get(url, headers=self.auth.headers)
        return handle_non_ok_status(r.status_code)

    def post(self, comment_id, object_id, from_datetime, to_datetime, comment):
        """
        Edit a comment attached to an object.

        POST /comments/{id}
        https://bbdata.daplab.ch/api/#comments__id__post
        """
        # TODO What is the diff between id and objectId? (comment id and obj id)
        #    and I think the comment could be clearer
        json = {
            "id": comment_id,
            "objectId": object_id,
            "from": from_datetime,
            "to": to_datetime,
            "comment": comment
        }
        url = output_api_url + self.base_path + "/" + str(comment_id)
        r = requests.post(url, json=json, headers=self.auth.headers)
        return handle_response(r.status_code, r.json())