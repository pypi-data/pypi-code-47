import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rangelist",
    version="0.0.3",
    author="Alexei M",
    author_email="alexeidjango@gmail.com",
    description="List of intersecting ranges",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexeidjango/rangelist",
    package_dir={'': 'rangelist'},
    packages=['rangelist'],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)