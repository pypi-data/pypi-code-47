from setuptools import setup
def readme():
     with open('README.md') as f:
        README = f.read()
     return README

setup(
    name="topsis_101703191",
    version="0.0.1",
    author="Geetansh Goyal",
    author_email="ggoyal_be17@thapar.edu",
    description="TOPSIS method",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/geetanshg22/topsis",
    packages=["topsis_101703191"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['scipy',
                      'tabulate',
                      'numpy',
                      'pandas'
     ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_101703191.topsis:main",
        ]
    },
)