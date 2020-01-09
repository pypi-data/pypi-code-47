import setuptools

with open("README.ctv", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aperturecore",
    version="0.0.6",
    author="LazyNeko",
    author_email="lazynekoo@gmail.com",
    description="A (unofficial) package for our Aperture Science Cores (tm)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LazyNeko1/ApertureCore",  # IS NOT PUBLIC YET
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)