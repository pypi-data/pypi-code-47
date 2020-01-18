import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="burrowswheeler",
    version="1.0",
    author="Fepe Laser",
    author_email="fepe55@gmail.com",
    description="Python implementation of the Burrows-Wheeler transform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fepe55/burrows-wheeler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
