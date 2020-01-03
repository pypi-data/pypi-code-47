import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smartwrappers",
    version="0.0.5",
    author="Cirill Usatchoff (Kyrylo Usachov)",
    author_email="usatchoff@gmail.com",
    description="A Python 3 library to manipulate objects with shared mutable wrappers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mavedev/SmartWrappers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)