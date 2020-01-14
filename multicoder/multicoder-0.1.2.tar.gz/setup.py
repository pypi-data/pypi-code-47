import codecs
import os.path
import re

from setuptools import find_packages, setup

# avoid a from multicoder import __version__ as version (that compiles multicoder.__init__ and is not compatible with bdist_deb)
version = None
for line in codecs.open(
    os.path.join("multicoder", "__init__.py"), "r", encoding="utf-8"
):
    matcher = re.match(r"""^__version__\s*=\s*['"](.*)['"]\s*$""", line)
    version = version or matcher and matcher.group(1)

# get README content from README.md file
with codecs.open(
    os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8"
) as fd:
    long_description = fd.read()

entry_points = {"console_scripts": ["multicoder = multicoder.cli:main"]}

setup(
    name="multicoder",
    version=version,
    description="Test classical encodings.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="flanker",
    author_email="github@19pouces.net",
    license="CeCILL-B",
    url="",
    entry_points=entry_points,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="multicoder.tests",
    install_requires=[],
    setup_requires=[],
    tests_requires=["hypothesis"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
