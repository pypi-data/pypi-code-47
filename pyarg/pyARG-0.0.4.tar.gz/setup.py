import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyARG",
    version="0.0.4",
    author="NexGen Analytics",
    author_email="info@ng-analytics.com",
    description="This repo contains the needed Python dependencies for ARG. Version 0.0.4 is only compatible with python 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
    ],
    python_requires='>=2.7,<3',
    install_requires=[requirements]
)
