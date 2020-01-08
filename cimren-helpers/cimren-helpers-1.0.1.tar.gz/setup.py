import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cimren-helpers",
    version="1.0.1",
    description="Helper functions",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/emrahcimren/helper_functions",
    author="cimren",
    author_email="cimren.1@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["helpers"],
    include_package_data=True,
    install_requires=["Pathlib"],
    #entry_points={
    #    "console_scripts": [
    #        "realpython=reader.__main__:main",
    #    ]
    #},
)
