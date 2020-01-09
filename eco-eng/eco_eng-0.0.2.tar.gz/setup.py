import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eco_eng", # Replace with your own username
    version="0.0.2",
    author="John Bolte",
    author_email="john.bolte@oregonstate.edu",
    description="Package for Ecological Engineering Applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OSU-BEE/eco-eng",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)