import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="socratagr",
    version="0.0.1",
    author="Example Author",
    author_email="digitalservices@grcity.us",
    description="Package to create, update, and delete data from The City of Grand Rapids instance of Socrata",
    long_description_content_type="text/markdown",
    url="https://github.com/GRInnovation/socrata_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
)