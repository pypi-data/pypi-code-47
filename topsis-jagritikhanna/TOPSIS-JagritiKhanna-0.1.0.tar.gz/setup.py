from setuptools import *

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="TOPSIS-JagritiKhanna",
    version="0.1.0",
    description="Topsis Analysis COE",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/TOPSIS-JagritiKhanna",
    author="Jagriti Khanna",
    author_email="jagriti.khanna31@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["TOPSIS_package"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "topsis=TOPSIS_package.cli:main",
        ]
    },
)
