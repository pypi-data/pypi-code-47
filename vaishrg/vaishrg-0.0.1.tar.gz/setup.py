import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vaishrg",
    version="0.0.1",
    author="Vaishnov RG",
    author_email="rgvaishnov9550@gmail.com",
    description="A sample python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vaishnovrg/python-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 