import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="garminconnect",
    version="0.1.1",
    author="Ron Klinkien",
    author_email="ron@cyberjunky.nl",
    description="Python 3 API wrapper for Garmin Connect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyberjunky/python-garminconnect",
    packages=["garminconnect"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
