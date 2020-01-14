import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yuzhuhwbubbler", 
    version="0.1.0",
    author="Yuzhu Wang", 
    author_email="15151843600@163.com", 
    description="A bubbler sort package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/e0431421/bubblewangyuzhu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
