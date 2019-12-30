import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kinCoke",
    version="0.0.2",
    author="Agustin Pardo",
    author_email="agustinmpardo@gmail.com",
    description="Greetings to you",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
)
