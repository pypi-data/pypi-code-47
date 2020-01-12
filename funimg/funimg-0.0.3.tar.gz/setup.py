import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name= "funimg", # Replace with your own username
    version="0.0.3",
    author="devhubyt",
    author_email="devhubyt@gmail.com",
    description="A small package to manipulate images with preloaded images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)