import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aestene-lib", # Replace with your own username
    version="0.0.1",
    author="Arnt Erik Stene",
    author_email="steneae@gmail.com",
    description="Package containing reusable tools for different applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aestene/AesLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)