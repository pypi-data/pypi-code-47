import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis-sunvir", # Replace with your own username
    version="0.0.1",
    author="Sunvir Singh",
    author_email="sunvirsingh72@gmail.com",
    description="python package to implement TOPSIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sunvir72/Topsis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
