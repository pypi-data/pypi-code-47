import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CopaData",
    version="3.40.1",
    author="COPA-DATA",
    author_email="development@copadata.com",
    description="Read metadata and online data from zenon Analyzer Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.copadata.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.7',
)