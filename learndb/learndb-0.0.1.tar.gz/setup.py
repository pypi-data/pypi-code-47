"""
Packaging script for learndb
"""
import setuptools
import learndb

# with open("README.md", "r") as fh:
    # long_description = fh.read()

setuptools.setup(
    name="learndb",
    version=learndb.VERSION,
    author="Microsoft Gray Systems Laboratory",
    author_email="learndb@microsoft.com",
    description="TBA",
    long_description="TBA",
    long_description_content_type="text/markdown",
    url="https://azuredata.microsoft.com/labs/gsl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
