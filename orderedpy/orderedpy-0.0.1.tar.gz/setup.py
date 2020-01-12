from setuptools import setup
import os


current_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_path, "README.rst"), encoding="utf-8") as file:
    long_description = file.read()

subpackages = []
parent = "orderedpy"
subpackages_path = os.path.join(current_path, "orderedpy")
for subdir, _, _ in os.walk(subpackages_path):
    subdirs = subdir.split(os.sep)
    parent_index = subdirs.index(parent) + 1
    subpackages.append(".".join(subdirs[parent_index:]))

setup(
    name="orderedpy",
    version="0.0.1",
    description="",
    long_description=long_description,
    url="https://github.com/monzita/orderedpy",
    author="Monika Ilieva",
    author_email="hidden@hidden.com",
    license='MIT License',
    keywords="orderedpy",
    packages=[*subpackages],
    package_data={},
    py_modules=["orderedpy"],
    install_requires=[],
    entry_points={"console_scripts": [],},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    zip_safe=True,
)
