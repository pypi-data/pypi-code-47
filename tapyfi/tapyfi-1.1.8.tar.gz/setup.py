from setuptools import setup


# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="tapyfi",
    version="1.1.8",
    description="Financial Indicators For Traders ",
    long_description="README",
    long_description_content_type="text/markdown",
    url="https://github.com/rdvnszn1/TaPyFi",
    author="Rıdvan Sözen",
    author_email="ridvansozen1@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['tapyfi', 'tapyfi.Helpers', "tapyfi.Indicators"],
    include_package_data=True,
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "tapyfi=tapyfi.__main__:main",
        ]
    },
)