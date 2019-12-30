#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_namespace_packages
import os

with open("README.rst") as readme_file:
    readme = readme_file.read()

# The requirements section should be kept in sync with the environment.yml file
requirements = [
    # fmt: off
    "click>=7.0",
    "click-plugins",
    "entrypoints",
    # fmt: on
]

setup_requirements = [
    # fmt: off
    "pytest-runner",
    "setuptools_scm",
    "wheel",
    # fmt: on
]

test_requirements = [
    # fmt: off
    "pytest>=3",
    "pytest-cov",
    # fmt: on
]

conda_rosetta_stone = {
    # fmt: off
    "pypa-requirement": "conda-dependency"
    # fmt: on
}

setup_kwargs = dict(
    author="Patrick Sodré",
    author_email="psodre@gmail.com",
    use_scm_version={"write_to": "zeroae/cli/_version.py"},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="ZeroAE's CLI",
    # fmt: off
    entry_points={
        "console_scripts": [
            "zeroae=zeroae.cli.cli:cli",
        ],
    },
    # fmt: on
    install_requires=requirements,
    license="MIT",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="cli zeroae",
    name="zeroae-cli",
    packages=find_namespace_packages(include=["zeroae.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={
        # fmt: off
        "test": test_requirements
        # fmt: on
    },
    url="https://github.com/zeroae/zeroae-cli",
    zip_safe=False,
)

if "CONDA_BUILD_STATE" in os.environ:
    try:
        from setuptools_scm import get_version

        setup_kwargs["version"] = get_version(**setup_kwargs["use_scm_version"])
        del setup_kwargs["use_scm_version"]
    except ModuleNotFoundError:
        print(
            "Error: zeroae-cli requires that setuptools_scm be installed with conda-build!"  # noqa: E501
        )
        raise
    setup_kwargs["conda_rosetta_stone"] = conda_rosetta_stone

setup(**setup_kwargs)
