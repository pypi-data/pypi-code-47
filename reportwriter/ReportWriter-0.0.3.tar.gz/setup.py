import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ReportWriter", # Replace with your own username
    version="0.0.3",
    author="Benjamin Saljooghi",
    author_email="benjamin.saljooghi@gmail.com",
    description="A small class for building strings and writing reports.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gist.github.com/benjaminsaljooghi/642fc730f4969ea5dba2d5cea360c04b",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)