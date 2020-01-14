from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "nq", "VERSION"), encoding="utf-8") as f:
    version = f.read()

setup(
    name="nq",
    version=version,
    description="Nested Queries",
    url="https://sgithub.fr.world.socgen/ktollec111518/nq",
    author="SG",
    author_email="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="dictionary nested query",
    packages=find_packages(include=["nq"]),
    package_data={'': ['nq/VERSION']},
    include_package_data=True,
    install_requires=[],
    extras_require={"tests": ["pytest", "flake8", "pytest-cov"]},
    entry_points={"console_scripts": []},
    project_urls={
        "Bug Reports": "https://sgithub.fr.world.socgen/ktollec111518/nq/issues",
        "Source": "https://sgithub.fr.world.socgen/ktollec111518/nq",
    },
)
