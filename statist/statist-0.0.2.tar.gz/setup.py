import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "statist",
    packages = ["statist"],
    entry_points = {
        "console_scripts": ['statist = statist.statist:statist']
        },
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = "0.0.2",
    description = "Get Todoist user stats in CLI",
    author = "Yoginth",
    author_email = "yoginth@protonmail.com",
    url = "https://yoginth.com",
    classifiers=(
        "Programming Language :: Python",
        "Natural Language :: English",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
    ),
    project_urls={
        'Source': 'https://gitlab.com/yo/statist'
    },
    install_requires=[
        'colorama',
        'todoist-python',
    ],
)
