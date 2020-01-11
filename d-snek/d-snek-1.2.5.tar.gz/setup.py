import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="d-snek",
    version="1.2.5",
    author="Jonathan de Jong",
    author_email="jonathan@automatia.nl",
    description="Discord SNEK framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.jboi.dev/ShadowJonathan/SNEK",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["discord.py>=1.2.5", "pony", "environs"],
    setup_requires=["wheel"],
    extras_require={
        "dev": ["ipython", "twine", "pymysql", "tox"],
        "lint": [
            "flake8==3.7.9",
            "isort==4.3.21",
            "mypy==0.740",
            "black==19.3b0",
            "flake8-bugbear>=19.8.0,<20",
            "docformatter>=1.3.1,<2",
        ],
    },
)
