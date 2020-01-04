# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['playlistzip']

package_data = \
{'': ['*']}

install_requires = \
['jsonpath-rw>=1.4,<2.0', 'pycurl>=7.43,<8.0']

entry_points = \
{'console_scripts': ['plz = playlistzip.cli:main']}

setup_kwargs = {
    'name': 'playlistzip',
    'version': '0.1.2',
    'description': 'Join two to four youtube playlists into viewsync links. Joining is accomplished by episode numbers, collected from video titles.',
    'long_description': 'playlistzip\n===========\n\nJoin two to four youtube playlists into combined viewsync links. Joining is accomplished either by episode numbers, collected from video titles, or by index pairing.\n\nSupports \\*nix and Windows.\n\nUsage\n--------\n\n.. code-block:: sh\n\n    plz "PL1O4GjhJgk40spOiTqpdh5rmp8z6lbpHQ" "PLlwKCy51_4YjSUB4gshARQIdFKOQ7wIqR"\n\nWhere positional arguments are *playlist* IDs retrieved from youtube. These are "list" GET parameters, visible in URL when you browse to any playlist page on youtube.\n\nYou can also specify regular expressions to be used to pick out episode numbers, directly via command line options. Useful for cases where default regex fail to get the correct episode number, or if you want to filter some videos out. All regular expressions have to contain one capturing group in them (specified by "([0-9]{1,2})" usually) -- capturing the episode number.\n\n.. code-block:: sh\n\n    plz --third-regex="Mathas ([0-9]{1,2})" \\\n        "PL1bauNEiHIgyqZ2B_x9kJWVX_dlDKv1cF" \\\n        "PLrIoJm0QOWUp-KwSJHNGGODWZCpVnu6km" \\\n        "PLH-huzMEgGWD5f_ItXeqF-qBoxkhNUNex"\n\nRegular expression options can be specified several times, it will try them until it gets a match, in order, starting with the first one.\n\n.. code-block:: sh\n\n    plz --third-regex="#([0-9]{1,2})" \\\n        --third-regex="Mathas ([0-9]{1,2})" \\\n        "PL1bauNEiHIgyqZ2B_x9kJWVX_dlDKv1cF" \\\n        "PLrIoJm0QOWUp-KwSJHNGGODWZCpVnu6km" \\\n        "PLH-huzMEgGWD5f_ItXeqF-qBoxkhNUNex"\n\nSynopsis:\n    plz [-h] [--first-regex FIRST_REGEX] [--second-regex SECOND_REGEX] [--third-regex THIRD_REGEX] [--fourth-regex FOURTH_REGEX] [--omit-title] [--json] [--join-by-index] playlists [playlists ...]\n\nFor each of joined episodes, output includes a title of the video of the first specified playlist, followed by viewsync URL.\n\n``--omit-title`` to get only viewsync URLs as an output.\n\n``--json`` output JSON instead of space separated data.\n\n``--join-by-index`` join playlists by index instead of using regex to match up episode numbers.\n\nContribute\n----------\n\n- Issue Tracker: gitlab.com/rossvor/playlistzip/issues\n- Source Code: gitlab.com/rossvor/playlistzip\n\nCopyright and License\n---------------------\nCopyright 2019, 2020 Ross Vorotynskij\n\nThe project is licensed under the GPL-3.0+ license.\n',
    'author': 'Ross Vorotynskij',
    'author_email': 'ross@rvcg.net',
    'url': 'https://gitlab.com/rossvor/playlistzip',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
