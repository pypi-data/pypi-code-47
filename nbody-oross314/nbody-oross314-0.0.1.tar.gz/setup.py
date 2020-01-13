import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbody-oross314", # Replace with your own username
    version="0.0.1",
    author="Olivia Ross",
    author_email="oross@ucsc.edu",
    description="Nbody simulation necessities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oross/nbody",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)