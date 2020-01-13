import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="macrobond-api-constants",
    version="1.0.2",
    author="Macrobond Financial",
    author_email="support@macrobond.com",
    description="Package with constants used by Macrobond API",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.macrobond.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=2.7',
)
