# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['spybar']

package_data = \
{'': ['*']}

install_requires = \
['psutil>=5.6.7,<6.0.0', 'tqdm>=4.41.1,<5.0.0']

entry_points = \
{'console_scripts': ['spybar = spybar.__main__:run']}

setup_kwargs = {
    'name': 'spybar',
    'version': '0.1.0',
    'description': 'Adds progress bars to any file-reading tool (gzip, md5sum, etc)',
    'long_description': "# Spybar\n\nSpybar is a Linux CLI utility that adds a progress bar to any tool reading a\nfile. By example, it can create a progress bar for `gzip`, `md5sum` and other\ntraditional utilities which don't display their progress.\n\nSimply prefix any command with `spybar`.\n\n```\nspybar gzip big_dump.sql\n```\n\nOr, if the process is already running, attach using its PID. Suppose that you\nwant to attach to process 42:\n\n```\nspybar -a 42\n```\n\n## FAQ\n\n### Can you pipe it?\n\nYes you can, the progress bar happens on `stderr`\n\n```\nspybar gzip -c big_dump.sql > big_dump.sql.gz\n```\n\n### Can it support Win/OSX?\n\nUnfortunately there is no known way to do so. This utility relies on `psutil`'s\n[`Process.open_files()`](https://psutil.readthedocs.io/en/latest/index.html#psutil.Process.open_files)\nabstraction so whenever this abstraction gives you the `position` for other\nplatforms than Linux then Spybar will automatically work on those.\n\n(By automatically I mean there is maybe a few adjustments needed on \nUnix-specific assumptions but it's most likely a just few lines to change).\n\n### How does it work?\n\nIf you navigate to the `/proc` file system you will see that for each process\nyou not only get the list of open files (in `/proc/XX/fd`) but also \nmeta-information about those files (in `/proc/XX/fdinfo`).\n\nThis way Spybar will look for files open in read mode by your process and then\nlook at the current position of the file pointer, which once compared to the\nfile size gives you the relative progress.\n\n### Does it always work?\n\nOf course not, but the use case of binaries reading a file from the beginning\nto the end is fairly common. Who never waited in front of a `gzip`, `xz`, `tar`\nor `md5sum` wondering if they should go have a coffee or if it's just 2 seconds\nmore?\n\nIn the end this is just guessing but it works in many situations.\n\n## Thanks\n\nI would like to thank:\n\n- Whomever put this feature in the Linux kernel\n- The `psutil` maintainers\n- The `tqdm` maintainers\n- The `poetry` maintainers\n- The `pytest` maintainers\n- All open-source contributors thanks to whom this software was easy to write\n\n## License\n\nThis software is released under the terms of the [WTFPL](./LICENSE).\n",
    'author': 'Rémy Sanchez',
    'author_email': 'remy.sanchez@hyperthese.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
