import re
import sys

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version_match = re.search(r'\d\.\d\.\d', ' '.join(sys.argv))
if version_match:
    version = version_match.group()
    sys.argv.remove(version)

    setuptools.setup(
        name="aiovkrmq",
        version=version,
        author="Mikhail Migushov",
        author_email="me@chuvash.pw",
        description="An async library to work with vkAPIService. Useless if you don't have the service.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://gitlab.com/gladbot/aiovkrmq",
        packages=['aiovkrmq'],
        install_requires=['aioamqp'],
        classifiers=[
            "Programming Language :: Python :: 3.7",
        ],
    )

else:
    print('ERROR: Version number in "X.Y.Z" format must be present in args')
    exit(1)
