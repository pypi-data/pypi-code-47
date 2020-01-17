from setuptools import setup, find_packages

MODULE_NAME = 'auxlibx'         # package name used to install via pip.

with open("README.md", "r") as fh:
    long_description = fh.read()


def requirements_from_pip(filename='requirements.txt'):
    with open(filename, 'r') as pip:
        return [l.strip() for l in pip if not l.startswith('#') and l.strip()]


setup(
    name=MODULE_NAME,
    version="0.0.1",
    author="Weld Lucas Cunha",
    author_email="cunha.lucas012@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    install_requires=requirements_from_pip(),
    extras_require={"test_deps": requirements_from_pip('requirements_test.txt')},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)