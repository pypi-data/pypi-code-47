import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-heideltime-krypton",
    version="0.0.1",
    author="Bharadwaj Srigiriraju",
    author_email="krishna.bharadwaj6@gmail.com",
    description="Python wrapper for Heideltime library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vetted/python-heideltime",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
