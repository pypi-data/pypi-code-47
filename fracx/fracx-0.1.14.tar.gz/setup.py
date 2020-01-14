# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fracx', 'fracx.api', 'fracx.collector', 'fracx.metrics', 'fracx.util']

package_data = \
{'': ['*'], 'fracx': ['data_files/*']}

install_requires = \
['aiocontextvars>=0.2.2,<0.3.0',
 'attr>=0.3.1,<0.4.0',
 'attrdict>=2.0.1,<3.0.0',
 'attrs>=19.3.0,<20.0.0',
 'click>=7.0,<8.0',
 'colorama>=0.4.3,<0.5.0',
 'coverage[toml]>=5.0.2,<6.0.0',
 'datadog>=0.33.0,<0.34.0',
 'flask-sqlalchemy>=2.4.1,<3.0.0',
 'json_log_formatter>=0.2.0,<0.3.0',
 'logutils>=0.3.5,<0.4.0',
 'psycopg2-binary>=2.8.4,<3.0.0',
 'pyparsing>=2.4.6,<3.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'python-dotenv>=0.10.3,<0.11.0',
 'pyyaml>=5.2,<6.0',
 'sqlalchemy>=1.3.12,<2.0.0',
 'tomlkit>=0.5.8,<0.6.0',
 'xlrd>=1.2.0,<2.0.0']

extras_require = \
{'mssql': ['pymssql>=2.1.4,<3.0.0', 'cython>=0.29.14,<0.30.0']}

entry_points = \
{'console_scripts': ['fracx = fracx.manage:main']}

setup_kwargs = {
    'name': 'fracx',
    'version': '0.1.14',
    'description': "FracX is a library that can be used to interface with PDS Energy's FracX platform for exchanging frac schedules.",
    'long_description': '# permian-frac-exchange\n\n<div style="text-align:center;">\n  <table >\n    <tr>\n      <a href="https://pypi.python.org/pypi/fracx/">\n        <img src="https://img.shields.io/pypi/pyversions/fracx.svg" />\n      </a>\n      <a href="https://codecov.io/gh/la-mar/permian-frac-exchange">\n        <img src="https://codecov.io/gh/la-mar/permian-frac-exchange/branch/master/graph/badge.svg" />\n      </a>\n      <a href="https://circleci.com/gh/la-mar/permian-frac-exchange">\n        <img src="https://circleci.com/gh/la-mar/permian-frac-exchange.svg?style=svg" />\n      </a>\n    </tr>\n\n  </table>\n</div>\n\n<p>The FracX Python library is a tool to interface with <a href=https://pdsenergy.com/frac-interference-exchange/>PDS Energy\'s</a> FracX platform, used to submit and download frac schedules. Currently, the project interfaces with the FTP import/export service provided by PDS. As other means of integration become available from PDS, those means will be incorporated into this project as additional ways to import and export data from FracX.</p>\n\nAvailable on PyPI and Docker\n\n<br/>\n\n## Installation\n\nInstall with pipx:\n\n```bash\npipx install fracx\n```\n\n   <br/>\n\n## Usage\n\n#### Set environment variables:\n\n```bash\n\nexport FRACX_FTP_USERNAME=my_fracx_username\nexport FRACX_FTP_PASSWORD=my_fracx_password\nexport FRACX_DATABASE_USERNAME=my_database_username\nexport FRACX_DATABASE_PASSWORD=my_database_passowrd\nexport FRACX_DATABASE_HOST=my.host.db\nexport FRACX_DATABASE_NAME=my_database\nexport FRACX_DATABASE_SCHEMA=my_schema\nexport FRACX_TABLE_NAME=frac_schedules\n\n```\n\n####\n\nInitialize the database:\n\n```bash\nfracx db init\n```\n\nInitialization creates one table and one view in the target database:\n\n- frac_schedules (or the value of FRACX_TABLE_NAME)\n- frac_schedules_by_api10 (or the value of FRACX_TABLE_NAME+"\\_by_api10")\n\nRe-running the db init command will attempt to create the table or view if one doesn\'t exist. It will NOT drop an existing table or view. This must be done manually.\n\n####\n\nRun the app:\n\n```bash\nfracx run collector\n```\n\nA successful execution will yield the following output:\n\n<pre>\n  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n                app config: fracx.config.ProductionConfig\n                flask app: fracx.manage.py\n                flask env: production\n                backend: postgres://fracx:***@db:5432/driftwood\n                collector: sftp.pdswdx.com\n  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nStarting download from sftp.pdswdx.com...\nDownload successful (download size: 70.58 KB, download_time: 0.0s)\nfrac_schedules.core_insert_update_on_conflict: inserted 625 records (1.28s)\n</pre>\n<br/>\n\n## Configuration Reference\n\nEnvironment variables reference:\n\n| name                    | default         | description                               |\n| ----------------------- | --------------- | ----------------------------------------- |\n| FRACX_FTP_URL           | sftp.pdswdx.com | url to the remote ftp server              |\n| FRACX_FTP_PORT          | 21              | port for the ftp server connection        |\n| FRACX_FTP_INPATH        | /Inbound        | ftp directory where uploads will be saved |\n| FRACX_FTP_OUTPATH       | /Outbound       | ftp directory to look for downloads in    |\n| FRACX_FTP_USERNAME      | ""              | username for ftp authentication           |\n| FRACX_FTP_PASSWORD      | ""              | password for ftp authentication           |\n| FRACX_DATABASE_USERNAME | ""              | username for database authentication      |\n| FRACX_DATABASE_PASSWORD | ""              | password for database authentication      |\n| FRACX_DATABASE_DIALECT  | postgres        | database dialect ("postgres" or "mssql")  |\n| FRACX_DATABASE_HOST     | localhost       | database host name                        |\n| FRACX_DATABASE_PORT     | 5432            | database port                             |\n| FRACX_DATABASE_NAME     | postgres        | database name                             |\n| FRACX_TABLE_NAME        | frac_schedules  | database table to store frac schedules    |\n\n<!--\nThe application can be configured with environment variables that are passed into the container at runtime. Environment variables can either be defined at the system level or in a file named \'.env\' in the project\'s root directory.\n<br/>\n\n### Saving output to a Postgres database\n\n<br/>\n\n##### Using a .env file\n\nExample configuration with .env file:\n\n.env\n\nWhen specifying configuration in a .env file, include it in docker-compose so the configuration is passed into the container at runtime.\n\ndocker-compose.yml\n\n```yaml\nversion: "3.7"\n\nservices:\n  collector:\n    image: driftwood/fracx\n    env_file: .env\n```\n\n<br/>\n<br/>\n##### Using docker-compose.yml\n\nExample configuration directly in the docker-compose.yml file:\n\n```yaml\nservices:\n  collector:\n    image: driftwood/fracx\n    environment:\n      FRACX_FTP_USERNAME: YOUR_FRACX_FTP_UERNAME\n      FRACX_FTP_PASSWORD: YOUR_FRACX_FTP_PASSWORD\n      FRACX_DATABASE_USERNAME: YOUR_DATABASE_USERNAME\n      FRACX_DATABASE_PASSWORD: YOUR_DATABASE_PASSWORD\n      FRACX_DATABASE_HOST: YOUR_DATABASE_HOST\n      FRACX_DATABASE_NAME: YOUR_DATABASE_NAME\n      FRACX_DATABASE_SCHEMA: fracx\n      FRACX_TABLE_NAME: frac_schedules\n``` -->\n',
    'author': 'Brock Friedrich',
    'author_email': 'brocklfriedrich@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/la-mar/permian-frac-exchange',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.5,<4.0.0',
}


setup(**setup_kwargs)
