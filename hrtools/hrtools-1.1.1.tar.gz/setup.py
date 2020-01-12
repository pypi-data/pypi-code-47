from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="hrtools",
    version="1.1.1",
    description="A Python package to get relevant information from HR data repositories.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/paulo663636/HRtools",
    author="Paulo Vinicius Antunes Sá de Oliveira",
    author_email="paulo.oliversa@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["hrtools"],
    include_package_data=True,
    install_requires=["requests","bs4","pandas"],
    entry_points={
        "console_scripts": [
            "hrtools=hrtools.glassdoor:main",
        ]
    },
)