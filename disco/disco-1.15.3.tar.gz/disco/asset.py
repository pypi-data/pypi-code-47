"""
Upload a file to DISCO, so it could later be used to run jobs.
"""
import io
import pathlib

import requests

from .base_controller import BaseController


class Asset(BaseController):
    """Provides functionality for uploading and downloading disco files"""

    def _request_url_for_upload(self, file_name, cluster_id=None):
        params = {'key': file_name}
        if cluster_id:
            params['clusterId'] = cluster_id
        return self.rest(url='/files/uploadparams',
                         data=params,
                         method='post'
                         )

    @classmethod
    def _upload(cls, url, file_name, form_fields, file_content_bytes):
        response = requests.request(
            'post',
            url,
            data=form_fields,
            files={
                'file': (file_name, io.BytesIO(file_content_bytes)),
            }
        )
        response.raise_for_status()

    def _register(self, token):
        return self.rest(
            url='/files',
            data={'token': token},
            method='post')['id']

    def upload(self, file_name, file, cluster_id=None):
        """Upload a file to DISCO, so it could later be used to run jobs.

        Args:
            file_name (str):
            file: `file` can be either the file contents,
                in binary or string forms, a file
                object, or a Path` object that points to a file.
            cluster_id (str):

        Returns:
            str: The id of the uploaded file.
        """
        if isinstance(file, bytes):
            file_content = file
        elif isinstance(file, str):
            file_content = file.encode()
        elif isinstance(file, pathlib.Path):
            file_content = file.read_bytes()
        elif hasattr(file, 'read'):
            file_content = file.read()
            if isinstance(file_content, bytes):
                pass
            elif isinstance(file_content, str):
                file_content = file_content.encode()
        else:
            file_content = pathlib.Path(str(file)).read_bytes()

        data = self._request_url_for_upload(file_name, cluster_id)
        self._upload(data['url'], file_name, form_fields=data['fields'],
                     file_content_bytes=file_content)
        register_result = self._register(data['token'])
        return register_result


def upload_file(file_name, file, cluster_id=None):
    """Legacy: Uploads file to DISCO, see `Assest.upload` for more info.

    Args:
        file_name (str):
        file: `file` can be either the file contents,
                in binary or string forms, a file
                object, or a Path` object that points to a file.
        cluster_id (str):

    Returns:
        str: The id of the uploaded file.
    """
    return Asset().upload(file_name, file, cluster_id=cluster_id)
