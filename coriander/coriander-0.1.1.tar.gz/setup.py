import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("src/coriander/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="coriander",
    version=version,
    project_urls={
        "Code": "https://github.com/odryfox/coriander",
        "Issue tracker": "https://github.com/odryfox/coriander/issues",
    },
    license="BSD-3-Clause",
    author="Vyacheslav Rusov",
    author_email="odryfox@gmail.com",
    description="A simple library for intent classification and named-entity recognition using templates.",
    long_description=readme,
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    extras_require={
        "dev": [
            "pytest",
            "sphinx",
        ],
        "docs": [
            "sphinx",
        ],
    },
)
