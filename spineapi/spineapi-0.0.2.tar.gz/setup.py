import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spineapi",
    version="0.0.2",
    author="northfoxz",
    author_email="firstera15@gmail.com",
    description="A simple machine learning inference library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spineapi/spine-api",
    packages=setuptools.find_packages(),
    install_requires=[
        "python-socketio[client]"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
