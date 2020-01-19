from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="topsis-yash-saxena",
    version="1.0.0",
    description="A Python pip package to apply topsis approach to rank the entries in a dataset",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yashsaxena972/topsis",
    author="Yash Saxena",
    author_email="yash972saxena@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["topsis_yash_saxena"],
    include_package_data=True,
    install_requires=["numpy "],
    entry_points={
        "console_scripts": [
            "topsis-yash-saxena=topsis_yash_saxena.cli:main",
        ]
    },
) 