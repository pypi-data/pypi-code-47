import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyCtrlLn", # Replace with your own username
    version="0.0.1",
    author="Hammie217",
    author_email="hammie217@gmail.com",
    description="A easy and quick consoling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hammie217/PyCtrl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
