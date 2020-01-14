# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vardbg', 'vardbg.output', 'vardbg.output.video_writer']

package_data = \
{'': ['*']}

install_requires = \
['dictdiffer>=0.8.1,<0.9.0',
 'jsonpickle>=1.2,<2.0',
 'opencv-python>=4.1.2,<5.0.0',
 'pillow>=7.0.0,<8.0.0',
 'sortedcontainers>=2.1.0,<3.0.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['pyrobud = vardbg.main:main']}

setup_kwargs = {
    'name': 'vardbg',
    'version': '0.10.1',
    'description': 'A simple Python debugger and profiler that generates animated visualizations of program flow.',
    'long_description': "# vardbg\n\nA simple Python debugger and profiler that generates animated visualizations of program flow.\n\n**Python 3.6** or newer is required due to the use of f-strings.\n\n## Features\n\n- Tracking the history of each variable and its contents\n- Tracking elements within containers (lists, sets, dicts, etc.)\n- Profiling the execution of each line\n- Summarizing all variables and execution times after execution\n- Passing arguments to debugged programs\n- Exporting execution history in JSON format and replaying (including program output)\n- Creating videos that show program flow, execution times, variables, and output\n- Writing videos in MP4 and GIF formats\n\n## Installation\n\nThe latest tagged version can be obtained from PyPI:\n\n```bash\npip install vardbg\n```\n\n## Usage\n\nAll of the program's options are documented in the usage help:\n\n```\n$ vardbg --help\nusage: vardbg [-h] [-f [FILE]] [-n [FUNCTION]] [-o [OUTPUT_FILE]] [-v [PATH]] [-c [CONFIG]]\n              [-a [ARGS [ARGS ...]]] [-p] [-P]\n\nA simple debugger that traces local variable changes, lines, and times.\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -f [FILE], --file [FILE]\n                        Python file to debug, or JSON result file to read\n  -n [FUNCTION], --function [FUNCTION]\n                        function to run from the given file (if applicable)\n  -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]\n                        path to write JSON output file to, default debug_results.json (will be truncated if it\n                        already exists and created otherwise)\n  -v [PATH], --video [PATH]\n                        path to write a video representation of the program execution to (MP4 and GIF formats\n                        are supported, depending on file extension)\n  -c [CONFIG], --video-config [CONFIG]\n                        path to the TOML config for the video output format, default video.toml\n  -a [ARGS [ARGS ...]], --args [ARGS [ARGS ...]]\n                        list of arguments to pass to the running program\n  -p, --absolute-paths  use absolute paths instead of relative ones\n  -P, --disable-live-profiler\n                        disable live profiler output during execution\n```\n\n## Comments\n\nSpecial comments can be added to lines of code that define variables to control how vardbg handles said variable:\n\n- `# vardbg: ignore` — do not display this variable or track its values\n",
    'author': 'Danny Lin',
    'author_email': 'danny@kdrag0n.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/CCExtractor/vardbg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
