
import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
	readme = f.read()

with io.open("src/skyz/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
	name="Skyz",
	version=version,
	url="https://github.com/pancubs/skyz",
	project_urls={
		"Documentation": "https://github.com/pancubs/skyz",
		"Code": "https://github.com/pancubs/skyz",
		"Issue tracker": "https://github.com/pancubs/skyz/issues"
	},
	license="BSD-3-Clause",
	author="Pancubs.org",
	author_email="dao@pancubs.org",
	maintainer="Pancubs.org",
	maintainer_email="dao@pancubs.org",
	description="A database API scraped from web.py.",
	classifiers=[
		"Intended Audience :: Developers",
		"License :: OSI Approved :: BSD License",
		"Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
	],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=[],
    extras_require={},
    entry_points={}
)