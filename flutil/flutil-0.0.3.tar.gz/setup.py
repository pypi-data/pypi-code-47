import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flutil",
    version="0.0.3",
    author="Floris De Feyter",
    author_email="floris.defeyter@kuleuven.be",
    description="Package with computer vision utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/EAVISE/flutil",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
