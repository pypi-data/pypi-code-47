"""
Fungsi untuk kompatibel dengan versi < 3.
"""

import sys

# pylint: disable=no-name-in-module;

if sys.version_info[0] > 2:
    # py3k
    from urllib.parse import urlparse, urljoin
else:
    # py2k
    from urllib import urlparse, urljoin
