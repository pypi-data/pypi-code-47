from setuptools import setup
import os


current_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_path, "README.rst"), encoding="utf-8") as file:
    long_description = file.read()

subpackages = []
parent = "octopy"
subpackages_path = os.path.join(current_path, "octopy")
for subdir, _, _ in os.walk(subpackages_path):
    subdirs = subdir.split(os.sep)
    parent_index = subdirs.index(parent) + 1
    subpackages.append(".".join(subdirs[parent_index:]))

setup(
    name="octopy",
    version="0.0.2",
    description="Github API Wrapper",
    long_description=long_description,
    url="https://github.com/monzita/octopy",
    author="Monika Ilieva",
    author_email="hidden@hidden.com",
    license="MIT License",
    keywords="octopy github wrapper api python3",
    packages=[*subpackages],
    package_data={},
    py_modules=["octopy"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    zip_safe=True,
)
