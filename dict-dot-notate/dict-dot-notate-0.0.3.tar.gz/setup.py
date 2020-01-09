from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dict-dot-notate", 
    version="0.0.3",
    author="Ddumba Kenneth",
    author_email="kjdumba@gmail.com",
    description="Turns nested dictionary keys to dotted strings with their corresponding values into a basic dictionary",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="dict notate dictdot dot",
    url="https://github.com/kenneth051/dict-dot-notate",
    packages=[
        "dot_notate"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)