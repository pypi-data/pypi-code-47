from setuptools import setup
def readme():
     with open('README.md') as f:
        README = f.read()
     return README

setup(
    name="topsis_101703295", # Replace with your own username
    version="0.0.1",
    author="Kshitiz varshney",
    author_email="kvarshney_be17@thapar.edu",
    description="A small example package",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/kv6737/topsis",
    packages=["topsis_101703295"],
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
            "topsis=topsis_101703295.topsis:main",
        ]
    },
)