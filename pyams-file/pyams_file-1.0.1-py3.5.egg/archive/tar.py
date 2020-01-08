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

"""PyAMS_file.archive.tar module

TAR files extraction module.
"""

import tarfile
from io import BytesIO

from pyams_file.file import get_magic_content_type
from pyams_file.interfaces.archive import IArchiveExtractor
from pyams_utils.registry import query_utility, utility_config


__docformat__ = 'restructuredtext'


@utility_config(name='application/x-tar', provides=IArchiveExtractor)
class TarArchiveExtractor:
    """TAR file format archive extractor"""

    tar = None

    def initialize(self, data, mode='r'):
        """Initialize extractor"""
        if isinstance(data, tuple):
            data = data[0]
        if not hasattr(data, 'read'):
            data = BytesIO(data)
        self.tar = tarfile.open(fileobj=data, mode=mode)

    def get_contents(self):
        """Extract archive contents"""
        members = self.tar.getmembers()
        for member in members:
            filename = member.name
            content = self.tar.extractfile(member)
            if content is not None:
                content = content.read()
            if not content:
                continue
            mime_type = get_magic_content_type(content[:4096])
            extractor = query_utility(IArchiveExtractor, name=mime_type)
            if extractor is not None:
                extractor.initialize(content)
                for element in extractor.get_contents():
                    yield element
            else:
                yield (content, filename)
