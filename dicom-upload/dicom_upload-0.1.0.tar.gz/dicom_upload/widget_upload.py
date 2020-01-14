#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juelich Supercomputing Centre (JSC).
# Distributed under the terms of the Modified BSD License.

"""
DICOM Upload Widget using the Jupyter Notebook Server RestAPI.
Uploads DICOM files with anonymized headers, i.e. the 0008 and 
0010 tags are removed on the JS side before the upload.

Files that aren't in DICOM format are ignored.

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


class Uploader(DescriptionWidget, ValueWidget):
    """Upload Widget. 

    Uploads DICOM files only via the Jupyter Notebook Server RestAPI,
    all other files will be ignored.
    DICOM files are anonymized by removing header tags starting with 
    0008 and 0010 on the JS side before uploading.

    The widget is able to upload large files by uploading them in chunks.
    The file contents will however not be directly available over the widget,
    but will have to be read into the notebook separately.

    """
    _model_name = Unicode('UploaderModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('UploaderView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    accept = Unicode(help='File types to accept, empty string for all').tag(sync=True)
    multiple = Bool(help='If True, allow for multiple files upload').tag(sync=True)
    disabled = Bool(help='Enable or disable button').tag(sync=True)
    icon = Unicode('upload', help="Font-awesome icon name, without the 'fa-' prefix.").tag(sync=True)
    button_style = CaselessStrEnum(
        values=['primary', 'success', 'info', 'warning', 'danger', ''], default_value='',
        help="""Use a predefined styling for the button.""").tag(sync=True)
    style = InstanceDict(ButtonStyle).tag(sync=True, **widget_serialization)
    metadata = List(Dict(), help='List of file metadata').tag(sync=True)

    # Needed for uploading using the Notebook Server RestAPI.
    token = Unicode(help='Jupyter API token').tag(sync=True)
    upload_url = Unicode('http://localhost:8888/api/contents/',
                        help='http(s)://notebook_url/api/contents/').tag(sync=True)

    # Variables set on the JavaScript side.
    files = List().tag(sync=True)
    responses = List().tag(sync=True)
    finished = Bool(False).tag(sync=True)
    hash = Unicode().tag(sync=True)
    _upload = Bool(False).tag(sync=True)

    
    def __init__(self, upload_url='http://localhost:8888/api/contents/', token='', *args, **kwargs):
        """Args:
            upload_url (str): Jupyter notebook URL appended by api/contents/<path>/. Directories on <path> must already exist.
            token (str): Jupyter notebook authentication token.
        """
        super(Uploader, self).__init__(*args, **kwargs)
        self.upload_url = upload_url
        self.token = token

    @default('description')
    def _default_description(self):
        return 'Upload'

    def upload(self):
        """Uploads file(s) via the JS fetch API."""
        self._upload = True