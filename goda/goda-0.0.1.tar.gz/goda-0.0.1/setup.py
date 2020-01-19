import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="goda",
    version="0.0.1",
    author="Pablo Sierra",
    author_email="pavelsjo@gmail.com",
    description="Python library to work with government open data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Charles-Darwing-Data-Community/goda",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)