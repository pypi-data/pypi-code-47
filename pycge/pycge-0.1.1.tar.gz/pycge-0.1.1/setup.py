import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
    name="pycge",
    version="0.1.1",
    author="Håvard Bønes",
    author_email="haavard.bones@gmail.com",
    description="A retro colored game engine for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/havbon/python-colored-game-engine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"
    ],
    python_requires='>=3.7'
)