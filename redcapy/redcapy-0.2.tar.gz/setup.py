import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redcapy",
    version="0.2",
    author="Unai Saralegui",
    author_email="usaralegui@gmail.com",
    description="Python package to access REDCAP API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/unaisaralegui/redcapy",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'lxml',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)