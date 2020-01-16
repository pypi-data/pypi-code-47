import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyFiFinder",
    version="0.0.22",
    author="M4rk(Marcelo almeida)",
    author_email="marcelorap345@gmail.com",
    description="this is a tool to search for archives by passing their specifc formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m4rkito/PyFiFinder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
