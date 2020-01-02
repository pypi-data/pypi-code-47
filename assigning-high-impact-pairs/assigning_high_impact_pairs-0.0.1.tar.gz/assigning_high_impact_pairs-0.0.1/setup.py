import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="assigning_high_impact_pairs", # Replace with your own username
    version="0.0.1",
    author="Robert Whiffin",
    author_email="robert.whiffin@tamr.com",
    description="A simple interface for getting high impact pairs from Tamr and assigning them.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Datatamer/personal/tree/master/robert.whiffin/get_high_impact_pair_details",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)