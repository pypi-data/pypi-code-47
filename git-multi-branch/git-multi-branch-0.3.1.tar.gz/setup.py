import setuptools

def install_requires():
    return ['click', 'gitpython', 'gitdb2']

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="git-multi-branch",
    version="0.3.1",
    author="bacox",
    author_email="bacox.dev@gmail.com",
    py_modules=['gitmb'],
    description="Clone all branches of a git repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bacox/git-multi-branch  ",
    install_requires=install_requires(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        git-multi-branch=gitmb:main
    """,
)