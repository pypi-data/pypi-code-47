# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['muni_is_api']

package_data = \
{'': ['*']}

install_requires = \
['coloredlogs>=10.0,<11.0',
 'defusedxml>=0.6.0,<0.7.0',
 'lxml>=4.4,<5.0',
 'requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'muni-is-api',
    'version': '0.8.0',
    'description': 'Python wrapper for the IS MUNI API',
    'long_description': '# IS MUNI API python wrapper\n\nPython wrapper for the IS MUNI API.\nThe IS MUNI Notes API documentation can be found [here](https://is.muni.cz/napoveda/technicka/bloky_api?lang=en).\n\nThe output format\n\n## Getting Started\n\nBuild status [![CircleCI](https://circleci.com/gh/pestanko/py-is-muni-api.svg?style=svg)](https://circleci.com/gh/pestanko/py-is-muni-api)\n\n### Prerequisites\n\n- requires Python 3.6 or higher\n\n### Install\n\n- Using [PIP](https://pypi.org/project/muni-is-api/):\n\n```bash\npip install muni-is-api\n```\n\n- Using the [Poetry](https://python-poetry.org/):\n\n\n```bash\npoetry add https://github.com/pestanko/py-is-muni-api.git\n```\n\n## Example\n\nExample usage of the IS API client\n\n```python\nimport muni_is_api\n\nclient = muni_is_api.IsApiClient(\n        domain=\'is.muni.cz\',\n        token=\'secret_token\',\n        faculty_id=1000,\n        course_code=\'PB000\'\n    )\n\n# Get na course info\ncourse_info = client.course_info()\n\n# Get list of students in the course\nstudents = client.course_list_students(registered=False, terminated=False, inactive=False)\n\n# Get list of stundets in the provided seminary\nsem_stud = client.seminar_list_students(seminars=[\'01\', \'02\'], terminated=False, inactive=False)\n\n# Get list of teachers for the provided seminary\nsem_teach = client.seminar_list_teachers(seminars=[\'01\', \'02\'])\n\n# Get list of all notepads for the course\nnotepads = client.notepad_list()\n\n# Get notepad content for the specified notepad shortcut and ucos\nnotepad_content = client.notepad_content(shortcut=\'hw01\', ucos=[1000, 1234, 12345])\n\n# Create a new notepad\nclient.notepad_new(name="Homework 01", shortcut="hw01", visible=True, complete=False, statistics=True)\n\n# Update a notepad\nclient.notepad_update(shortcut="hw01", uco=1000, content="Great work! *2", override=True)\n\n# List all exams\nexams = client.exams_list(terminated=False, inactive=False)\n```\n\n\n\n',
    'author': 'Peter Stanko',
    'author_email': 'peter.stanko0@gmail.com',
    'url': 'https://github.com/pestanko/py-is-muni-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
