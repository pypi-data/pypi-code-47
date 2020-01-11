import re
import sys

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version_match = re.search(r'\d\.\d\.\d', ' '.join(sys.argv))
if version_match:
    version = version_match.group()
    sys.argv.remove(version)

else:
    print('ERROR: Version number in "X.Y.Z" format must be present in args')
    exit(1)
    version = None

setuptools.setup(
    name="vkapi_rmq_client",
    version=version,
    author="Mikhail Migushov",
    author_email="me@chuvash.pw",
    description="A library to work with vkAPIService. Useless if you don't have the service.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyber-chuvash/vkAPIClient",
    packages=['vkapi'],
    install_requires=['pika'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)
