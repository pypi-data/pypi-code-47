from setuptools import setup

version = "v1.0.1"
setup(
    name="ppvt",
    python_requires=">3.5.1",
    version=version,
    description="Checks for latest package versions",
    keywords="ppvt",
    author="chatrapathi",
    author_email="chatrapati.k7@gmail.com",
    url="https://github.com/chatrapathik/python-package-version-tool.git",
    license="MIT License",
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"console_scripts": ["ppvt = pypi:run"]},
)
