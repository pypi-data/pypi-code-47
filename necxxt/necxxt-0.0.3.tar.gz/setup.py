import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join("necxxt", "version.py"), "r") as f:
    exec(f.read())

setuptools.setup(
    name="necxxt",
    version=__version__,
    author="Marius Meisenzahl",
    author_email="mariusmeisenzahl@gmail.com",
    description="The package manager for next level C++ projects",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/necxxt/cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    scripts=["bin/necxxt"],
)
