# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['herakles', 'herakles.jql', 'herakles.util']

package_data = \
{'': ['*']}

install_requires = \
['PyYaml>=5.0,<6.0', 'jira>=2.0,<3.0']

setup_kwargs = {
    'name': 'herakles',
    'version': '0.1.4',
    'description': 'Tools for working with the python jira client.',
    'long_description': '# herakles jira tool\n\nTools for working with the [Jira API](https://jira.readthedocs.io/en/master/index.html).\n\n\n## Usage\n\n### Initialize\n\n```python\nfrom herakles import JiraAuthBasic, JiraWrapper\nauth = JiraAuthBasic("username", "password")\njira = JiraWrapper.connect("https://server.jira.com", auth)\n\n# optional add map of custom fields.\njira.add_custom_fields_from_file("custom_fields.yml")\n```\n\n### Use jql builder to programmatically build jql queries\n\nSee how many tickets a user resolved in the past number days:\n```python\nquery = {\n            "and": [\n                {"assignee": {"=": team_member}},\n                {"resolved": {">": f"-{days}d"}},\n                {"project": {"not in": ["\'Unrelated Project\'"]}},\n            ]\n        }\n```\n\n## Contributors Guide\n\n### Testing\n\nTesting is done via pytest.\n\n```\n$ pip install -r requirements.txt\n$ pytest\n```\n\nTo get code coverage information, you can run pytest directly.\n\n```\n$ pip install -r requirements.txt\n$ pytest --cov=src --cov-report=html\n```\n\nThis will generate an html coverage report in `htmlcov/` directory.\n',
    'author': 'David Bradford',
    'author_email': 'david.bradford@mongodb.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dbradf/herakles-jira-client',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
