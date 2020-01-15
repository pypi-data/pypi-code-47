from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ReportWriter", # Replace with your own username
    version="0.0.8",
    author="Benjamin Saljooghi",
    author_email="benjamin.saljooghi@gmail.com",
    description="A small class for building strings and writing reports.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benjaminsaljooghi/reportwriter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    packages=["reportwriter"],
    package_data={
        "reportwriter": ["py.typed", "*.pyi"],
    },
)

