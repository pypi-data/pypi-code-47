from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="moopy",
    version="0.0.5", # Update __init__.py if the version changes!
    author="Derk Kappelle",
    author_email="20672345+dkappelle@users.noreply.github.com",
    description="A package for Multi-Objective Optimization tools",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/moo4all/MooPy.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
