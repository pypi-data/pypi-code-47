import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fakerlocationer',
    version='0.3',
    scripts=['fakerlocationer.py'],
    author="kenevil1",
    author_email="no@email.com",
    description="A simple class that can be used to fake Selenium Browser Geolocation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kenevil1/fakerlocationer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)