#
# Copyright (c) 2008-2015 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_file.archive.gz module

GZip files extraction module.
"""

import gzip
from io import BytesIO

from pyams_file.archive.tar import TarArchiveExtractor
from pyams_file.file import get_magic_content_type
from pyams_file.interfaces.archive import IArchiveExtractor
from pyams_utils.registry import utility_config


__docformat__ = 'restructuredtext'


@utility_config(name='application/x-gzip', provides=IArchiveExtractor)
class GZipArchiveExtractor:
    """GZip file format archive extractor"""

    data = None
    gzip_file = None

    def initialize(self, data):
        """Initialize extractor"""
        if isinstance(data, tuple):
            data = data[0]
        if not hasattr(data, 'read'):
            data = BytesIO(data)
        self.data = data
        self.gzip_file = gzip.GzipFile(fileobj=data, mode='r')

    def get_contents(self):
        """Extract archive contents"""
        gzip_data = self.gzip_file.read(4096)
        mime_type = get_magic_content_type(gzip_data)
        if mime_type == 'application/x-tar':
            tar = TarArchiveExtractor()
            tar.initialize(self.data, mode='r:gz')
            for element in tar.get_contents():
                yield element
        else:
            next_data = self.gzip_file.read()
            while next_data:
                gzip_data += next_data
                next_data = self.gzip_file.read()
            yield (gzip_data, '')
