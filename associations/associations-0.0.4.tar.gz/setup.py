import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="associations",
    version="0.0.4",
    author="Hyppoprogramm",
    author_email="programm.jeremiah@yandex.ru",
    description="Assocition management package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/associations",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
