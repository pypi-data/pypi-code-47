import os
import sys
import setuptools

from setuptools import setup
from setuptools.command.install import install
# from circleci.version import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != '0.9.9':
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, '0.9.9'
            )
            sys.exit(info)

setuptools.setup(
    name="flashlexiot",
    version="0.9.9",
    author="Clay Graham",
    author_email="claytantor@flashlex.com",
    description="Flashlex IOT for python makes it easy to make any python computer an IOT device.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/claytantor/flashlex-iot-python",
    packages=setuptools.find_packages(),
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", 
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>=3.4',
    cmdclass={
        'verify': VerifyVersionCommand,
    }

)
