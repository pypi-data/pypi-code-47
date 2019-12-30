import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leglight", 
    version="0.0.1",
    author="Jon Davis / Obviate.io",
    author_email="python-code@obviate.io",
    description="A Python module designed to control the Elgato brand Lights.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/obviate.io/pyleglight",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=["elgato", "key light", "corsair"],
)