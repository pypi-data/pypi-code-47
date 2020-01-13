import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
with open("requirements.txt", "r") as fh:
    REQUIREMENTS = fh.readlines()
with open("linky/VERSION", "r") as fh:
    VERSION = fh.read().strip()

setuptools.setup(
    name="linky-db",
    version=VERSION,
    author="LoveIsGrief",
    author_email="loveisgrief@tuta.io",
    description="A script to manage and tag files using symlinks",
    install_requires=REQUIREMENTS,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/NamingThingsIsHard/linky",
    packages=setuptools.find_packages(
        exclude=["tests", "tests.*"]
    ),
    package_data={
        "linky": [
            "VERSION",
            "schemas/*.yaml"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: POSIX :: Linux",
    ],
    project_urls={
        "Bug Tracker": "https://gitlab.com/NamingThingsIsHard/linky/issues",
    },
    entry_points={
        "console_scripts": [
            "linky = linky.app:main",
        ]
    }
)
