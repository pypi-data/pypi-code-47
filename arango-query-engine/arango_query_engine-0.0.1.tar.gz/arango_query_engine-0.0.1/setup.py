import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arango_query_engine", # Replace with your own username
    version="0.0.1",
    author="hooman hedayti",
    author_email="hham.group12@gmail.com",
    description="A python library for quering in ArangoDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent", #only tested on opensuse tumbelweed
    ],
    python_requires='>=3.7',
)