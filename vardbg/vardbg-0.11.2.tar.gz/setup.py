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
 'pygments>=2.5.2,<3.0.0',
 'sortedcontainers>=2.1.0,<3.0.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['pyrobud = vardbg.main:main']}

setup_kwargs = {
    'name': 'vardbg',
    'version': '0.11.2',
    'description': 'A simple Python debugger and profiler that generates animated visualizations of program flow.',
    'long_description': "# vardbg\n\nA simple Python debugger and profiler that generates animated visualizations of program flow.\n\n**Python 3.6** or newer is required due to the use of f-strings.\n\nThis project was created during [Google Code-in](https://codein.withgoogle.com/) 2019 for [CCExtractor Development](https://ccextractor.org/).\n\n## Features\n\n- Tracking the history of each variable and its contents\n- Tracking elements within containers (lists, sets, dicts, etc.)\n- Ignoring specific variables\n- Profiling the execution of each line\n- Summarizing all variables and execution times after execution\n- Passing arguments to debugged programs\n- Exporting execution history in JSON format and replaying (including program output)\n- Creating videos that show program flow, execution times, variables (with relationships), and output\n- Writing videos in MP4, GIF, and WebP formats\n\n## Demo\n\n![Demo Video](https://user-images.githubusercontent.com/7930239/72677173-77345580-3a4e-11ea-9968-dae3eee7d122.gif)\n\n## Installation\n\nThe latest tagged version can be obtained from PyPI:\n\n```bash\npip install vardbg\n```\n\n## Usage\n\nAll of the program's options are documented in the usage help:\n\n```\n$ vardbg --help\nusage: vardbg [-h] [-f [FILE]] [-n [FUNCTION]] [-o [OUTPUT_FILE]] [-v [PATH]] [-c [CONFIG]]\n              [-a [ARGS [ARGS ...]]] [-p] [-P]\n\nA simple debugger that traces local variable changes, lines, and times.\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -f [FILE], --file [FILE]\n                        Python file to debug, or JSON result file to read\n  -n [FUNCTION], --function [FUNCTION]\n                        function to run from the given file (if applicable)\n  -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]\n                        path to write JSON output file to, default debug_results.json (will be truncated if it\n                        already exists and created otherwise)\n  -v [PATH], --video [PATH]\n                        path to write a video representation of the program execution to (MP4 and GIF formats\n                        are supported, depending on file extension)\n  -c [CONFIG], --video-config [CONFIG]\n                        path to the TOML config for the video output format, default video.toml\n  -a [ARGS [ARGS ...]], --args [ARGS [ARGS ...]]\n                        list of arguments to pass to the running program\n  -p, --absolute-paths  use absolute paths instead of relative ones\n  -P, --disable-live-profiler\n                        disable live profiler output during execution\n```\n\nFor example, this command will debug the function `quick_sort` from the file `sort.py` with the arguments `9 3 5 1` and create a JSON file called `sort1.json`:\n\n```bash\nvardbg -f sort.py -n quick_sort -o sort1.json -a 9 3 5 1\n```\n\nA video can then be generated from the above JSON:\n\n```bash\nvardbg -f sort1.json -v sort_vis.mp4\n```\n\nIt is possible to generate videos live while running the debugged program, but this is discouraged because the overhead of video creation inflates execution times greatly and thus ruins profiler results. However, if profiling is not important to you, it is a valid use case.\n\n## Comments\n\nSpecial comments can be added to lines of code that define variables to control how vardbg handles said variable:\n\n- `# vardbg: ignore` — do not display this variable or track its values\n- `# vardbg: ref lst[i]` — treat variable `i` as the index/key of an element in container `lst` (only shown in videos)\n\n## Contributing\n\nFeel free to contribute to this project! You can add features, fix bugs, or make any other improvements you see fit. We just ask that you follow the [code style guidelines](https://github.com/CCExtractor/vardbg/blob/master/CODE_STYLE.md) to keep the code consistent and coherent. Once your contribution meets the guidelines, [open a pull request](https://github.com/CCExtractor/vardbg/compare) to make things official.\n",
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
