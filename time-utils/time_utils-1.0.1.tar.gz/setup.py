import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="time_utils",
    version="1.0.1",
    author="Joe Hanna",
    description="Helper class to time python processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hannaj06/time_utils",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
