from setuptools import setup
import os


current_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_path, "README.rst"), encoding="utf-8") as file:
    long_description = file.read()

subpackages = []
parent = "newpyfile"
subpackages_path = os.path.join(current_path, "newpyfile")
for subdir, _, _ in os.walk(subpackages_path):
    subdirs = subdir.split(os.sep)
    parent_index = subdirs.index(parent) + 1
    subpackages.append(".".join(subdirs[parent_index:]))

from newpyfile import VERSION

setup(
    name="newpyfile",
    version=VERSION,
    description="Create .py files from your cli.",
    long_description=long_description,
    url="https://github.com/monzita/newpyfile",
    author="Monika Ilieva",
    author_email="hidden@hidden.com",
    license="MIT",
    keywords="newpyfile file python",
    packages=[*subpackages],
    package_data={},
    py_modules=["newpyfile file python"],
    install_requires=["docopt"],
    entry_points={"console_scripts": ["newpyfile=newpyfile.cli:main"],},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=True,
)
