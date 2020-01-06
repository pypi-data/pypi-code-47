# <copyright>

"""
"""

from setuptools import setup, find_packages


setup(
    name="cresbot",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    author="Matthew Dowdell",
    author_email="matthew.dowdell@gmail.com",
    description="A library for interacting with the RuneScape and RuneScape Wiki APIs.",
    url="https://gitlab.com/weirdgloop/cresbot-lib",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["dataclasses; python_version < '3.7'", "requests"],
)
