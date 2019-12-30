import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dnssplitter",
    version="1.0.0",
    author="Wes Hardaker",
    author_email="opensource@hardakers.net",
    description="A fast python implementation of breaking down DNS domains into parts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hardaker/dnssplitter",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'dnssplit = dnssplitter.scripts.dnssplit:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3',
    test_suite='nose.collector',
    tests_require=['nose'],
)
