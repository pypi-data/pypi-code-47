import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ReportWriter", # Replace with your own username
    version="0.0.7",
    author="Benjamin Saljooghi",
    author_email="benjamin.saljooghi@gmail.com",
    description="A small class for building strings and writing reports.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benjaminsaljooghi/reportwriter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
