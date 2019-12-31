import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="git-client",
    version="0.2.0",
    author="Andy Klier",
    author_email="andyklier@gmail.com",
    description="gc is a command line helper client for using git.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/shindagger/git-client",
    packages=['gitclient'],
    include_package_data=True,
    install_requires= ['setuptools', 'inquirer', 'string-color>=0.2.7'],
    entry_points = {
        'console_scripts': ['gc=gitclient.main:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
