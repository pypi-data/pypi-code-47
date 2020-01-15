import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req:
    requires = req.read().strip().split('\n')

setuptools.setup(
    name="betfair_python_rest",
    version="0.12",
    author="Anton Igin",
    author_email="antonigin1995@gmail.com",
    description="Python package of REST API managers (Betting and Accounts APIs)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Sibiryakanton/betfair_python_rest',
    packages=setuptools.find_packages(),
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    project_urls={
        'Source': 'https://github.com/Sibiryakanton/betfair_python_rest',
    },
)
