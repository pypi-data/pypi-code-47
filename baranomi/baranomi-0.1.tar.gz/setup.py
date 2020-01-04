import os
import codecs
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command



here = os.path.abspath(os.path.dirname(__file__))

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

class UploadCommand(Command):
    """Support setup.py publish."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except FileNotFoundError:
            pass
        self.status("Building Source distribution…")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))
        self.status("Uploading the package to PyPi via Twine…")
        os.system("sudo twine upload dist/*")
        sys.exit()



setup(
    name = "baranomi",
    version="0.1",
    author = "Kevin Hill",
    author_email = "kah.kevin.hill@gmail.com",
    description = ("Split and join files."),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    py_modules=['baranomi'],
    packages=find_packages(),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[],
    cmdclass={"upload": UploadCommand},
)