import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="overpython",
    version="1.0.1",
    author="supernova",
    author_email="tomfleetwitter@gmail.com",
    description="A pointless package designed to overcomplicate Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/host12prog/overpython/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
