import os
from setuptools import setup, find_packages
import uuid

from jirafs_csv_table import __version__ as version_string


requirements_path = os.path.join(
    os.path.dirname(__file__),
    'requirements.txt',
)
try:
    from pip.req import parse_requirements
    requirements = [
        str(req.req) for req in parse_requirements(
            requirements_path,
            session=uuid.uuid1()
        )
    ]
except (ImportError, AttributeError, ValueError, TypeError):
    requirements = []
    with open(requirements_path, 'r') as in_:
        requirements = [
            req for req in in_.readlines()
            if not req.startswith('-')
            and not req.startswith('#')
        ]


setup(
    name='jirafs_csv_table',
    version=version_string,
    url='https://github.com/coddingtonbear/jirafs-csv-table',
    description="Include tables in your Jira comments or description using a local CSV file.",
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        'jirafs_plugins': [
            'csv_table = jirafs_csv_table.plugin:Plugin',
        ]
    },
)
