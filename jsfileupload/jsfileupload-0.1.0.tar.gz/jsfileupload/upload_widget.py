#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juelich Supercomputing Centre (JSC).
# Distributed under the terms of the Modified BSD License.

"""
FileUpload Widget using the Jupyter Notebook Server RestAPI.
Can handle large files by uploading files in chunks.
"""
from ipywidgets import ValueWidget
from ipywidgets import register, widget_serialization
from ipywidgets.widgets.trait_types import InstanceDict
from ipywidgets.widgets.widget_button import ButtonStyle
from ipywidgets.widgets.widget_description import DescriptionWidget

from traitlets import (
     default, Unicode, Dict, List, Int, Bool, Bytes, CaselessStrEnum
)
from ._frontend import module_name, module_version


class FileUpload(DescriptionWidget, ValueWidget):
    """FileUpload Widget. Uploads via the Jupyter Notebook Server RestAPI.

    The widget is able to upload large files by uploading them in chunks.
    The file contents will however not be directly available over the widget,
    but will have to be read into the notebook seperately.
    """
    _model_name = Unicode('FileUploadModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('FileUploadView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    accept = Unicode(help='File types to accept, empty string for all').tag(sync=True)
    multiple = Bool(help='If True, allow for multiple files upload').tag(sync=True)
    disabled = Bool(help='Enable or disable button').tag(sync=True)
    icon = Unicode('folder', help="Font-awesome icon name, without the 'fa-' prefix.").tag(sync=True)
    button_style = CaselessStrEnum(
        values=['primary', 'success', 'info', 'warning', 'danger', ''], default_value='',
        help="""Use a predefined styling for the button.""").tag(sync=True)
    style = InstanceDict(ButtonStyle).tag(sync=True, **widget_serialization)
    metadata = List(Dict(), help='List of file metadata').tag(sync=True)

    # Needed for uploading using the Notebook Server RestAPI.
    token = Unicode(help='Jupyter API token').tag(sync=True)
    upload_url = Unicode('http://localhost:8888/api/contents/',
                        help='http(s)://<notebook_url>/api/contents/<path>').tag(sync=True)

    # Variables set on the JavaScript side.
    files = List().tag(sync=True)
    responses = List().tag(sync=True)
    finished = Bool(False).tag(sync=True)
    _upload = Bool(False).tag(sync=True)

    
    def __init__(self, upload_url='http://localhost:8888/api/contents/', token='', *args, **kwargs):
        """Args:
            upload_url (str): Jupyter notebook URL appended by api/contents/<path>/. Directories on <path> must already exist.
            token (str): Jupyter notebook authentication token.
        """
        super(FileUpload, self).__init__(*args, **kwargs)
        self.upload_url = upload_url
        self.token = token

    @default('description')
    def _default_description(self):
        return 'Browse'

    def upload(self):
        """Uploads file(s) via the JS fetch API."""
        self._upload = True