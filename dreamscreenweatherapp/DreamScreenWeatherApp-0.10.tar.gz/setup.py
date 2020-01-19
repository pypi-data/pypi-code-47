import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DreamScreenWeatherApp", # Replace with your own username
    version="0.10",
    author="John Tashiro",
    author_email="jtashiro@fiospace.com",
    description="An interface to Weather Underground, as a data source for the HP DreamScreen weather app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/jtashiro/dreamscreen-weather/src/master/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
