import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qmspy",
    version="0.0.12",
    author="Brian C. Ferrari",
    author_email="brianf1996@knights.ucf.edu",
    description="This is a python module for analysing and graphing QMS data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cavenfish/qmspy",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "scipy", "pandas", "seaborn",
                      "openpyxl", "matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
