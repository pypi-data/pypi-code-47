import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cargs",
    version="0.0.1",
    author="Beomsoo Kim",
    author_email="bluewhale8202@gmail.com",
    description="A commandline arguments parsing Library with"\
                " an extremely simple interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bombs-kim/cargs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
