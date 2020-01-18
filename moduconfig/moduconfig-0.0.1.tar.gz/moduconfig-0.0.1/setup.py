import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moduconfig",
    version="0.0.1",
    author="Omar Nasr",
    author_email="omar@omarnasr.ca",
    description=(
        "A declarative and powerful configuration API" +
        "for application configuration and documentation"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Moro-Code/moduconfig",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires=">=3.5"
)
