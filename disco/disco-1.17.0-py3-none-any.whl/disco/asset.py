"""
Upload a file to DISCO, so it could later be used to run jobs.
"""
import io
import os
import pathlib
import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

from disco.core import create_progress_bar, constants
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
    def _upload_with_callback(cls, url, file_name, form_fields, file_content_bytes, callback):
        """
        Upload file with callback for monitoring the progress

        Args:
            url (str):
            file_name (str):
            form_fields (dict):
            file_content_bytes (bytes):
            callback (func):
        """
        encoder = MultipartEncoder({
            **form_fields,
            'file': (file_name, io.BytesIO(file_content_bytes)),
        })
        monitor = MultipartEncoderMonitor(encoder, callback)
        response = requests.request(
            'post',
            url,
            data=monitor,
            headers={'Content-Type': monitor.content_type}
        )
        response.raise_for_status()

    def _register(self, token):
        return self.rest(
            url='/files',
            data={'token': token},
            method='post')['id']

    def upload(self, file_name, file, cluster_id=None, show_progress_bar=True):
        """Upload a file to DISCO, so it could later be used to run jobs.

        Args:
            file_name (str):
            file: `file` can be either the file contents,
                in binary or string forms, a file
                object, or a Path` object that points to a file.
            cluster_id (str):
            show_progress_bar (bool):

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

        disable_progress_bar = os.environ.get(constants.ENV_VAR_DISABLE_PROGRESS_BAR) == '1' or (not show_progress_bar)

        with create_progress_bar(
                total=len(file_content),
                desc=f"Uploading {file_name}", unit='B',
                ncols=80, disable=disable_progress_bar, unit_scale=True) as progress_bar:

            update_progress_bar_callback = self.__create_update_progress_bar_callback(progress_bar)

            self._upload_with_callback(data['url'],
                                       file_name,
                                       form_fields=data['fields'],
                                       file_content_bytes=file_content,
                                       callback=update_progress_bar_callback)

        register_result = self._register(data['token'])
        return register_result

    @staticmethod
    def __create_update_progress_bar_callback(progress_bar):
        context = dict(bytes_read_so_far=0)

        def update_progress_bar_callback(monitor):
            new_bytes_read = monitor.bytes_read
            current_delta = new_bytes_read - context['bytes_read_so_far']
            context['bytes_read_so_far'] = new_bytes_read
            progress_bar.update(current_delta)

        return update_progress_bar_callback


def upload_file(file_name, file, cluster_id=None, show_progress_bar=True):
    """Legacy: Uploads file to DISCO, see `Assest.upload` for more info.

    Args:
        file_name (str):
        file: `file` can be either the file contents,
                in binary or string forms, a file
                object, or a Path` object that points to a file.
        cluster_id (str):
        show_progress_bar (bool):

    Returns:
        str: The id of the uploaded file.
    """
    return Asset().upload(file_name, file, cluster_id=cluster_id, show_progress_bar=show_progress_bar)
