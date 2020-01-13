import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyHeap",
    version="0.0.2",
    author="Sammyalhashe",
    author_email="sammy.alhashemi@mail.utoronto.ca",
    description="A small heap implementation with customizeable key",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sammyalhashe/PyHeap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
