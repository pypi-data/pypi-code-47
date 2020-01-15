#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing",
    "Topic :: Text Processing :: General",
    "Topic :: Text Processing :: Markup :: HTML",
    "Topic :: Text Processing :: Markup",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Internet :: WWW/HTTP :: Site Management",
    "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    "Topic :: Internet :: WWW/HTTP"
]

setup(
    name="asha",
    version="0.0.4",
    maintainer="Shanu Khera",
    maintainer_email="kherashanu@gmail.com",
    author="Shanu Khera",
    author_email="kherashanu@gmail.com",
    url="https://github.com/khera-shanu/asha",
    license="MIT",
    platforms=["any"],
    include_package_data=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=[
        "rangeen>=0.0.1",
        "Jinja2>=2.10.3",
        "markdown2>=2.3.8",
        "htmlmin>=0.1.12",
    ],
    entry_points={"console_scripts": ["asha = asha:main"]},
    description="An unicode and ascii colour, emotes, art and loader library for terminals.",
    classifiers=classifiers,
    long_description="""A static site generator for lazy developers."""
)
