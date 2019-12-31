import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_mortgage",
    version="0.2.3",
    author="tdsprogramming",
    description="A package to handle mortgage calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tdsprogramming/py-mortgage",
    packages=setuptools.find_packages(),
    install_requires = [
        'pandas>=0.25.3'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
