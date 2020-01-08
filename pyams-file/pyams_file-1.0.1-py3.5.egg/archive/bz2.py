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

"""PyAMS_file.archive.bz2 module

Bzip2 extraction module.
"""

import bz2

from pyams_file.archive.tar import TarArchiveExtractor
from pyams_file.file import get_magic_content_type
from pyams_file.interfaces.archive import IArchiveExtractor
from pyams_utils.registry import utility_config


__docformat__ = 'restructuredtext'


CHUNK_SIZE = 4096


@utility_config(name='application/x-bzip2', provides=IArchiveExtractor)
class BZip2ArchiveExtractor:
    """BZip2 file format archive extractor"""

    data = None
    bz2 = None

    def initialize(self, data):
        """Initialize extractor"""
        if isinstance(data, tuple):
            data = data[0]
        self.data = data
        self.bz2 = bz2.BZ2Decompressor()

    def get_contents(self):
        """Extract archive contents"""
        position = 0
        compressed = self.data[position:position + CHUNK_SIZE]
        decompressed = self.bz2.decompress(compressed)
        while (not decompressed) and (position < len(self.data)):
            compressed = self.data[position:position + CHUNK_SIZE]
            decompressed = self.bz2.decompress(compressed)
            position += CHUNK_SIZE
        mime_type = get_magic_content_type(decompressed[:CHUNK_SIZE])
        if mime_type == 'application/x-tar':
            tar = TarArchiveExtractor()
            tar.initialize(self.data, mode='r:bz2')
            for element in tar.get_contents():
                yield element
        else:
            while position < len(self.data):
                compressed = self.data[position:position + CHUNK_SIZE]
                decompressed += self.bz2.decompress(compressed)
                position += CHUNK_SIZE
            yield (decompressed, '')
