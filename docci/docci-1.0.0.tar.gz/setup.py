# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docci']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.0,<4.0']

setup_kwargs = {
    'name': 'docci',
    'version': '1.0.0',
    'description': 'Various document utils',
    'long_description': '# docci\n\nVarious document management utils\n\n## Usage\n\nThe `docci.file.FileAttchment` class is root of whole package. \nIt abstracts work with files and provides useful properties like base64 convertion, content-disposition header generation, mimetype detection:\n\n```python\nfrom docci.file import FileAttachment\n\n# Create file attachment from file\nfile = FileAttachment.load("path/to/file")\n\n# Now you can use the FileAttachment features:\n# Get base64 file representation\nfile.content_base64\n\n# Generate Content-Disposition header with file name\nfile.content_disposition\n\n# Get file extension\nfile.extension\n\n# Get file mimetype\nfile.mimetype\n\n# Save file to disk\nfile.save("path/to/file")\n```  \n\nTo see other features proceed to the [documentation](https://docci.readthedocs.io/en/latest/) ',
    'author': 'potykion',
    'author_email': 'potykion@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/potykion/docci',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
